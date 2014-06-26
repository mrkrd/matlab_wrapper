# -*- coding: utf-8 -*-
"""
Copyright 2010-2013 Joakim Möller
Copyright 2014 Marek Rudnicki

This file is part of matlab_wrapper.

matlab_wrapper is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

matlab_wrapper is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with matlab_wrapper.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import print_function, division, absolute_import

import numpy as np
import platform
from os.path import join, dirname, isfile, realpath
import os
import warnings

import ctypes
from ctypes import c_char_p, POINTER, c_size_t, c_bool, c_void_p, c_int

from matlab_wrapper.typeconv import dtype_to_mat

class mxArray(ctypes.Structure):
    pass

class Engine(ctypes.Structure):
    pass

mwSize = c_size_t
mwIndex = c_size_t


wrap_script = r"""
ERRSTR__ = '';
try
    {0}
catch err
    ERRSTR__ = sprintf('%s: %s\n', err.identifier, err.message);
    for i = 1:length(err.stack)
        ERRSTR__ = sprintf('%sError: in fuction %s in file %s line %i\n', ERRSTR__, err.stack(i,1).name, err.stack(i,1).file, err.stack(i,1).line);
    end
end
if exist('ERRSTR__','var') == 0
    ERRSTR__='';
end
"""

class MatlabSession(object):
    """Matlab session.

    Parameters
    ----------
    options : str, optional
        Options that will be passed to MATLAB at the start,
        e.g. '-nosplash'.
    matlab_root : str or None, optional
        Root of the MATLAB installation.  If unsure, then start MATLAB
        and type `matlabroot`.  If `None`, then will be determined
        based on the `matlab` binary location.
    buffer_size : int, optional
        MATLAB output buffer size.  The output buffer can be accessed
        through `output_buffer` property.

    Attributes
    ----------
    output_buffer : str
        Access to the MATLAB output buffer.
    workspace : Workspace object
        Easy access to MATLAB workspace, e.g. `workspace.sin([1.,2.,3.])`.
    version : str
        MATLAB version number.

    Methods
    -------
    get()
    put()
    eval()

    """
    def __init__(self, options='-nosplash', matlab_root=None, buffer_size=0):
        system = platform.system()

        if matlab_root is None:
            matlab_root = find_matlab_root()
        lib_dir = find_lib_dir(matlab_root)

        if matlab_root is None:
            raise RuntimeError("MATLAB location is unknown (try to initialize MatlabSession with matlab_root properly set)")

        self._matlab_root = matlab_root


        ### Load libraries the libraries
        if system == 'Linux':
            self._libeng = ctypes.CDLL(
                join(lib_dir, 'libeng.so')
            )
            self._libmx = Library(
                join(lib_dir, 'libmx.so')
            )

            command = "{executable} {options}".format(
                executable=join(matlab_root, 'bin', 'matlab'),
                options=options
            )

        elif system=='Windows':
            if lib_dir not in os.environ['PATH']:
                os.environ['PATH'] = lib_dir + ';' + os.environ['PATH']

            self._libeng = ctypes.CDLL('libeng')
            self._libmx = Library('libmx')

            command = None

        else:
            raise NotImplementedError("System {} not yet supported.".format(system))




        ### Setup function types for args and returns
        ## libeng
        self._libeng.engOpen.argtypes = (c_char_p,)
        self._libeng.engOpen.restype = POINTER(Engine)
        self._libeng.engOpen.errcheck = error_check

        self._libeng.engPutVariable.argtypes = (POINTER(Engine), c_char_p, POINTER(mxArray))
        self._libeng.engPutVariable.restype = c_int
        self._libeng.engPutVariable.errcheck = error_check

        self._libeng.engGetVariable.argtypes = (POINTER(Engine), c_char_p)
        self._libeng.engGetVariable.restype = POINTER(mxArray)
        self._libeng.engGetVariable.errcheck = error_check

        self._libeng.engEvalString.argtypes = (POINTER(Engine), c_char_p)
        self._libeng.engEvalString.restype = c_int
        self._libeng.engEvalString.errcheck = error_check

        self._libeng.engOutputBuffer.argtypes = (POINTER(Engine), c_char_p, c_int)
        self._libeng.engOutputBuffer.restype = c_int


        ## libmx
        self._libmx.mxGetNumberOfDimensions.argtypes = (POINTER(mxArray),)
        self._libmx.mxGetNumberOfDimensions.restype = mwSize

        self._libmx.mxGetDimensions.argtypes = (POINTER(mxArray),)
        self._libmx.mxGetDimensions.restype = POINTER(mwSize)

        self._libmx.mxGetNumberOfElements.argtypes = (POINTER(mxArray),)
        self._libmx.mxGetNumberOfElements.restype = c_size_t

        self._libmx.mxGetElementSize.argtypes = (POINTER(mxArray),)
        self._libmx.mxGetElementSize.restype = c_size_t

        self._libmx.mxGetClassName.argtypes = (POINTER(mxArray),)
        self._libmx.mxGetClassName.restype = c_char_p

        self._libmx.mxIsNumeric.argtypes = (POINTER(mxArray),)
        self._libmx.mxIsNumeric.restype = c_bool

        self._libmx.mxIsCell.argtypes = (POINTER(mxArray),)
        self._libmx.mxIsCell.restype = c_bool

        self._libmx.mxIsComplex.argtypes = (POINTER(mxArray),)
        self._libmx.mxIsComplex.restype = c_bool

        self._libmx.mxGetData.argtypes = (POINTER(mxArray),)
        self._libmx.mxGetData.restype = POINTER(c_void_p)
        self._libmx.mxGetData.errcheck = error_check

        self._libmx.mxGetImagData.argtypes = (POINTER(mxArray),)
        self._libmx.mxGetImagData.restype = POINTER(c_void_p)
        self._libmx.mxGetImagData.errcheck = error_check

        self._libmx.mxGetCell.argtypes = (POINTER(mxArray), mwIndex)
        self._libmx.mxGetCell.restype = POINTER(mxArray)
        ### Errors has to be handled elswhere, because of NULL on uninitialized cells
        # self._libmx.mxGetCell.errcheck = error_check

        self._libmx.mxSetCell.argtypes = (POINTER(mxArray), mwIndex, POINTER(mxArray))
        self._libmx.mxSetCell.restype = None

        self._libmx.mxGetNumberOfFields.argtypes = (POINTER(mxArray),)
        self._libmx.mxGetNumberOfFields.restype = c_int
        self._libmx.mxGetNumberOfFields.errcheck = error_check

        self._libmx.mxGetFieldNameByNumber.argtypes = (POINTER(mxArray), c_int)
        self._libmx.mxGetFieldNameByNumber.restype = c_char_p
        self._libmx.mxGetFieldNameByNumber.errcheck = error_check

        self._libmx.mxGetField.argtypes = (POINTER(mxArray), mwIndex, c_char_p)
        self._libmx.mxGetField.restype = POINTER(mxArray)
        ### Errors has to be handled elswhere, because of NULL on uninitialized fields
        # self._libmx.mxGetField.errcheck = error_check

        self._libmx.mxSetField.argtypes = (POINTER(mxArray), mwIndex, c_char_p, POINTER(mxArray))
        self._libmx.mxSetField.restype = None

        self._libmx.mxCreateStructArray.argtypes = (mwSize, POINTER(mwSize), c_int, POINTER(c_char_p))
        self._libmx.mxCreateStructArray.restype = POINTER(mxArray)
        self._libmx.mxCreateStructArray.errcheck = error_check

        self._libmx.mxArrayToString.argtypes = (POINTER(mxArray),)
        self._libmx.mxArrayToString.restype = c_char_p
        self._libmx.mxArrayToString.errcheck = error_check

        self._libmx.mxCreateString.argtypes = (c_char_p,)
        self._libmx.mxCreateString.restype = POINTER(mxArray)
        self._libmx.mxCreateString.errcheck = error_check

        self._libmx.mxGetString.argtypes = (POINTER(mxArray), c_char_p, mwSize)
        self._libmx.mxGetString.restype = c_int
        self._libmx.mxGetString.errcheck = error_check

        self._libmx.mxCreateNumericArray.argtypes = (mwSize, POINTER(mwSize), c_int, c_int)
        self._libmx.mxCreateNumericArray.restype = POINTER(mxArray)
        self._libmx.mxCreateNumericArray.errcheck = error_check

        self._libmx.mxCreateLogicalArray.argtypes = (mwSize, POINTER(mwSize))
        self._libmx.mxCreateLogicalArray.restype = POINTER(mxArray)
        self._libmx.mxCreateLogicalArray.errcheck = error_check

        self._libmx.mxCreateCellArray.argtypes = (mwSize, POINTER(mwSize))
        self._libmx.mxCreateCellArray.restype = POINTER(mxArray)
        self._libmx.mxCreateCellArray.errcheck = error_check

        self._libmx.mxDestroyArray.argtypes = (POINTER(mxArray),)
        self._libmx.mxDestroyArray.restype = None


        ### Start the engine
        self._ep = self._libeng.engOpen(command)


        ### Setup the output buffer
        if buffer_size != 0:
            self._output_buffer = ctypes.create_string_buffer(buffer_size)
            self._libeng.engOutputBuffer(
                self._ep,
                self._output_buffer,
                buffer_size-1
            )
        else:
            self._output_buffer = None


        ### Workspace object
        self.workspace = Workspace(self)


        ### Check MATLAB version
        version = self.version
        if ('R2014a' in version) and system == 'Linux':
            warnings.warn("You are using MATLAB version R2014a on Linux, which appears to have a bug in engGetVariable().  You will only be able to use arrays of type double.")




    def __del__(self):
        self._libeng.engClose(self._ep)


    @property
    def output_buffer(self):
        if self._output_buffer is None:
            raise RuntimeError("Output buffer was not initialized properly.")
        else:
            return self._output_buffer.value


    def eval(self, expression):
        """Evaluate `expression` in MATLAB engine.

        Parameters
        ----------
        expression : str
            Expression is passed to MATLAB engine and evaluated.

        """
        expression_wrapped = wrap_script.format(expression)


        ### Evaluate the expression
        self._libeng.engEvalString(self._ep, expression_wrapped)

        ### Check for exceptions in MATLAB
        mxresult = self._libeng.engGetVariable(self._ep, 'ERRSTR__')

        error_string = self._libmx.mxArrayToString(mxresult)

        if error_string != "":
            raise RuntimeError("Error from MATLAB\n{0}".format(error_string))



    def get(self, name):
        """Get variable `name` from MATLAB workspace.

        Parameters
        ----------
        name : str
            Name of the variable in MATLAB workspace.

        Returns
        -------
        array_like
            Value of the variable `name`.

        """
        pm = self._libeng.engGetVariable(self._ep, name)

        out = mxarray_to_ndarray(self._libmx, pm)


        self._libmx.mxDestroyArray(pm)

        return out




    def put(self, name, value):
        """Put a variable to MATLAB workspace.

        """

        pm = ndarray_to_mxarray(self._libmx, value)

        self._libeng.engPutVariable(self._ep, name, pm)

        self._libmx.mxDestroyArray(pm)


    @property
    def version(self):
        """Return string representing MATLAB version."""

        self.eval("VERSION__ = version")
        ver = self.get('VERSION__')
        self.eval("clear VERSION__")

        return ver



    def __repr__(self):
        r = '<MatlabSession:{root}>'.format(root=self._matlab_root)

        return r



def error_check(result, func, arguments):
    if (isinstance(result, c_int) and result != 0) or (isinstance(result, POINTER(mxArray)) and not bool(result)):
        raise RuntimeError(
            "MATLAB function {func} failed ({result}) with arguments:\n{arguments}".format(
                func=str(func),
                result=str(result),
                arguments=str(arguments)
            ))
    return result



def find_matlab_root():
    """Look for matlab binary and return root directory of MATLAB
    installation.

    """
    matlab_root = None

    path_dirs = os.environ.get("PATH").split(os.pathsep)
    for path_dir in path_dirs:
        candidate = realpath(join(path_dir, 'matlab'))
        if isfile(candidate) or isfile(candidate + '.exe'):
            matlab_root = dirname(dirname(candidate))
            break

    return matlab_root


def find_lib_dir(matlab_root):
    """Locate the directory where libraries are located, which is OS and
    architecture dependent.

    """
    bits, linkage = platform.architecture()
    system = platform.system()

    if (system == 'Linux') and (bits == '64bit'):
        lib_dir = join(matlab_root, "bin", "glnxa64")
    # elif (system == 'Linux') and (bits == '32bit'):
    #     lib_dir = join(matlab_root, "bin", "glnx86")
    elif (system == 'Windows') and (bits == '64bit'):
        lib_dir = join(matlab_root, "bin", "win64")
    # elif (system == 'Windows') and (bits == '32bit'):
    #     lib_dir = join(matlab_root, "bin", "win32")
    else:
        raise RuntimeError("Unsopported OS or architecture: {} {}".format(system, bits))

    return lib_dir


class Workspace(object):
    def __init__(self, session):
        self._session = session


    def __getattr__(self, attr):

        session = self._session

        session.eval("KIND__ = exist('{}')".format(attr))
        kind = session.get('KIND__')
        session.eval("clear KIND__")

        if kind == 0:
            raise RuntimeError("No such variable/function in MATLAB workspace: {}".format(attr))

        elif kind == 1:         # Variable
            out = session.get(attr)

        elif kind in (2, 3, 5, 6): # Function
            out = MatlabFunction(name=attr, session=self._session)

        else:
            raise NotImplementedError("Unknown variable/function type in MATLAB workspace: {}".format(attr))

        return out


    def __setattr__(self, name, value):

        if name.startswith('_'):
            object.__setattr__(self, name, value)
        else:
            self._session.put(name, value)



class MatlabFunction(object):
    def __init__(self, name, session):
        self.name = name
        self._session = session

    def __call__(self, *args, **kwargs):
        session = self._session


        ### Left-hand side (returns) string
        nout = kwargs.get('nout', 1)
        outs = ["OUT{}__".format(i) for i in range(nout)]
        outs_str = ','.join(outs)


        ### Right hand side (arguments) string
        ins = []
        for i,a in enumerate(args):
            aname = "ARG{}__".format(i)
            session.put(aname, a)
            ins.append(aname)
        ins_str = ','.join(ins)


        ### MATLAB command
        if outs:
            cmd = "[{outs}] = {name}({ins})".format(
                outs=outs_str,
                name=self.name,
                ins=ins_str
            )
        else:
            cmd = "{name}({ins})".format(
                name=self.name,
                ins=ins_str
            )


        ### Run the function
        session.eval(cmd)


        ### Clear input variables in MATLAB
        if ins:
            session.eval("clear {}".format(' '.join(ins)))


        ### Get the resulst from MATLAB
        rets = []
        for o in outs:
            r = session.get(o)
            rets.append(r)


        ### Clear the resutls in MATLAB
        if outs:
            session.eval("clear {}".format(' '.join(outs)))


        ### Return the results
        if len(rets) == 1:
            ret = rets[0]
        else:
            ret = tuple(rets)

        return ret

    @property
    def __doc__(self):

        session = self._session

        session.eval(
            "DOC__ = help('{}')".format(self.name)
        )

        doc = session.get('DOC__')

        session.eval("clear DOC__")

        return doc



def mxarray_to_ndarray(libmx, pm):
    """Convert MATLAB object `pm` to numpy equivalent."""

    ndims = libmx.mxGetNumberOfDimensions(pm)
    dims = libmx.mxGetDimensions(pm)
    numelems = libmx.mxGetNumberOfElements(pm)
    elem_size = libmx.mxGetElementSize(pm)
    class_name = libmx.mxGetClassName(pm)
    is_numeric = libmx.mxIsNumeric(pm)
    is_complex = libmx.mxIsComplex(pm)
    data = libmx.mxGetData(pm)
    imag_data = libmx.mxGetImagData(pm)


    if is_numeric:
        datasize = numelems*elem_size

        real_buffer = ctypes.create_string_buffer(datasize)
        ctypes.memmove(real_buffer, data, datasize)
        pyarray = np.ndarray(
            buffer=real_buffer,
            shape=dims[:ndims],
            dtype=class_name,
            order='F'
        )

        if is_complex:
            imag_buffer = ctypes.create_string_buffer(datasize)
            ctypes.memmove(imag_buffer, imag_data, datasize)
            pyarray_imag = np.ndarray(
                buffer=imag_buffer,
                shape=dims[:ndims],
                dtype=class_name,
                order='F'
            )

            pyarray = pyarray + pyarray_imag * 1j

        out = pyarray.squeeze()

        if out.ndim == 0:
            out, = np.atleast_1d(out)


    elif class_name == 'char':
        datasize = numelems + 1

        pystring = ctypes.create_string_buffer(datasize+1)
        libmx.mxGetString(pm, pystring, datasize)

        out = pystring.value


    elif class_name == 'logical':
        datasize = numelems*elem_size

        buf = ctypes.create_string_buffer(datasize)
        ctypes.memmove(buf, data, datasize)

        pyarray = np.ndarray(
            buffer=buf,
            shape=dims[:ndims],
            dtype='bool',
            order='F'
        )

        out = pyarray.squeeze()
        if out.ndim == 0:
            out, = np.atleast_1d(out)


    elif class_name == 'cell':
        out = []
        for i in range(numelems):
            cell = libmx.mxGetCell(pm, i)

            if bool(cell):
                o = mxarray_to_ndarray(libmx, cell)
            else:
                ### uninitialized cell
                o = None

            out.append(o)

        out = np.array(out, dtype='O')
        out = out.reshape(dims[:ndims], order='F')
        out = out.squeeze()


    elif class_name == 'struct':
        field_num = libmx.mxGetNumberOfFields(pm)

        ### Get all field names
        field_names = []
        for i in range(field_num):
            field_name = libmx.mxGetFieldNameByNumber(pm, i)
            field_names.append(field_name)

        ### Get all fields
        records = []
        for i in range(numelems):
            record = []
            for field_name in field_names:
                field = libmx.mxGetField(pm, i, field_name)

                if bool(field):
                    el = mxarray_to_ndarray(libmx, field)
                else:
                    ### uninitialized cell
                    el = None

                record.append(el)
            records.append(record)


        ### Set the dtypes right (if there is any ndarray, we want dtype=object)
        arrays = zip(*records)
        new_arrays = []
        for arr in arrays:
            contains_ndarray = np.any([isinstance(el, np.ndarray) for el in arr])

            ## This loop is necessary, because np.rec.fromarrays()
            ## cannot handle well a list of arrays of the same size
            if contains_ndarray:
                newarr = np.empty(len(arr), dtype='O')
                for i,a in enumerate(arr):
                    newarr[i] = a

            else:
                newarr = np.array(arr)

            new_arrays.append(newarr)

        out = np.rec.fromarrays(new_arrays, names=field_names)
        out = out.reshape(dims[:ndims], order='F')
        out = out.squeeze()


    else:
        raise NotImplementedError('{}-arrays are not supported'.format(class_name))


    return out




def ndarray_to_mxarray(libmx, arr):

    if isinstance(arr, str):
        pm = libmx.mxCreateString(arr)

    elif isinstance(arr, dict):
        raise NotImplementedError('dicts are not supported.')

    else:
        arr = np.array(arr, ndmin=2)


    if isinstance(arr, np.ndarray) and arr.dtype.kind in ['i','u','f','c']:
        dim = arr.ctypes.shape_as(mwSize)
        complex_flag = (arr.dtype.kind == 'c')

        pm = libmx.mxCreateNumericArray(
            arr.ndim,
            dim,
            dtype_to_mat(arr.dtype),
            complex_flag
        )

        mat_data = libmx.mxGetData(pm)
        np_data = arr.real.tostring('F')
        ctypes.memmove(mat_data, np_data, len(np_data))

        if complex_flag:
            mat_data = libmx.mxGetImagData(pm)
            np_data = arr.imag.tostring('F')
            ctypes.memmove(mat_data, np_data, len(np_data))


    elif isinstance(arr, np.ndarray) and arr.dtype.kind == 'b':
        dim = arr.ctypes.shape_as(mwSize)

        pm = libmx.mxCreateLogicalArray(arr.ndim, dim)

        mat_data = libmx.mxGetData(pm)
        np_data = arr.real.tostring('F')
        ctypes.memmove(mat_data, np_data, len(np_data))


    elif isinstance(arr, np.ndarray) and arr.dtype.kind in ('O', 'S'):
        dim = arr.ctypes.shape_as(mwSize)

        pm = libmx.mxCreateCellArray(arr.ndim, dim)

        for i,el in enumerate(arr.flatten('F')):
            p = ndarray_to_mxarray(libmx, el)
            libmx.mxSetCell(pm, i, p)


    elif isinstance(arr, np.ndarray) and len(arr.dtype) > 0:
        dim = arr.ctypes.shape_as(mwSize)

        name_num = len(arr.dtype.names)

        names_p = (c_char_p*name_num)(*[c_char_p(name) for name in arr.dtype.names])

        pm = libmx.mxCreateStructArray(
            arr.ndim,
            dim,
            name_num,
            names_p,
        )

        for i,record in enumerate(arr.flatten('F')):
            for name in arr.dtype.names:
                el = record[name]
                p = ndarray_to_mxarray(libmx, el)

                libmx.mxSetField(pm, i, name, p)

    elif isinstance(arr, np.ndarray):
        raise NotImplementedError('Type {} not supported.'.format(arr.dtype))

    return pm



class Library(object):
    """Shared library proxy.

    The purpouse of this class is to wrap CDLL objects and append
    `_730` to function names on the fly.  It should resolve the int vs
    mwSize problems for those functions.

    """
    def __init__(self, *args, **kwargs):
        self._lib = ctypes.CDLL(*args, **kwargs)

    def __getattr__(self, attr):

        attr730 = attr + '_730'

        try:
            out = getattr(self._lib, attr730)
        except AttributeError:
            out = getattr(self._lib, attr)

        return out
