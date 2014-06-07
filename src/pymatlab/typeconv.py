# -*- coding: iso-8859-15 -*-
'''
Copyright 2010-2013 Joakim Möller

This file is part of pymatlab.

pymatlab is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pymatlab is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pymatlab.  If not, see <http://www.gnu.org/licenses/>.
'''

from ctypes import *
from numpy import array,ndarray,dtype
from os.path import join
import platform
import sys,numpy

def numpy_to_ctype(np_variable):
    dtype = str(np_variable.dtype)
    ctype = c_double
    if "uint" in dtype:
        if '8' in dtype:
            ctype = c_ubyte
        elif '16' in dtype:
            ctype = c_ushort
        elif '32' in dtype:
            ctype = c_uint
        elif '64' in dtype:
            ctype = c_ulong
    elif "int" in dtype:
        if '8' in dtype:
            ctype = c_byte
        elif '16' in dtype:
            ctype = c_short
        elif '32' in dtype:
            ctype = c_int
        elif '64' in dtype:
            ctype = c_long
    elif "float" in dtype:
        if '32' in dtype:
            ctype = c_float
        elif '64' in dtype:
            ctype = c_double
        else:
            ctype = c_double
    return ctype

def mat_to_ctype(classname):
    dtype = classname
    ctype = c_double
    if "uint" in dtype:
        if '8' in dtype:
            ctype = c_ubyte
        elif '16' in dtype:
            ctype = c_ushort
        elif '32' in dtype:
            ctype = c_uint
        elif '64' in dtype:
            ctype = c_ulong
    elif "int" in dtype:
        if '8' in dtype:
            ctype = c_byte
        elif '16' in dtype:
            ctype = c_short
        elif '32' in dtype:
            ctype = c_int
        elif '64' in dtype:
            ctype = c_long
    elif "single" in dtype:
        ctype = c_float
    elif "double" in dtype:
        ctype = c_double
    return ctype


def np_to_mat(np_variable):
    
    #Typedef enum
    #{
    #0        mxUNKNOWN_CLASS = 0,
    #1        mxCELL_CLASS,
    #2        mxSTRUCT_CLASS,
    #3        mxLOGICAL_CLASS,
    if np_variable.dtype.type ==numpy.bool:
        matlab_type = c_int(3)
    #4        mxCHAR_CLASS,
    elif np_variable.dtype.type ==numpy.str :
        matlab_type = c_int(4)
    #5        mxVOID_CLASS,
    elif np_variable.dtype.type ==numpy.void:
        matlab_type = c_int(5)
    #6        mxDOUBLE_CLASS,
    elif np_variable.dtype.type ==numpy.complex128: 
        matlab_type = c_int(6)
    elif np_variable.dtype.type ==numpy.float64: 
        matlab_type = c_int(6)
    #7        mxSINGLE_CLASS,
    elif np_variable.dtype.type ==numpy.complex64: 
        matlab_type = c_int(7)
    elif np_variable.dtype.type ==numpy.float32: 
        matlab_type = c_int(7)
    #8        mxINT8_CLASS,
    elif np_variable.dtype.type ==numpy.int8: 
        matlab_type = c_int(8)
    #9        mxUINT8_CLASS,
    elif np_variable.dtype.type ==numpy.uint8: 
        matlab_type = c_int(9)
    #10       mxINT16_CLASS,
    elif np_variable.dtype.type ==numpy.int16: 
        matlab_type = c_int(10)
    #11       mxUINT16_CLASS,
    elif np_variable.dtype.type ==numpy.uint16: 
        matlab_type = c_int(11)
    #12       mxINT32_CLASS,
    elif np_variable.dtype.type ==numpy.int32: 
        matlab_type = c_int(12)
    #13       mxUINT32_CLASS,
    elif np_variable.dtype.type ==numpy.uint32: 
        matlab_type = c_int(13)
    #14       mxINT64_CLASS,
    elif np_variable.dtype.type ==numpy.int64: 
        matlab_type = c_int(14)
    #15       mxUINT64_CLASS,
    elif np_variable.dtype.type ==numpy.uint64: 
        matlab_type = c_int(15)
    #16       mxFUNCTION_CLASS,
    #17       mxOPAQUE_CLASS,
    #18       mxOBJECT_CLASS, /* keep the last real item in the list */
    #        #if defined(_LP64) || defined(_WIN64)
    #        mxINDEX_CLASS = mxUINT64_CLASS,
    #        #else
    #        mxINDEX_CLASS = mxUINT32_CLASS,
    #        #endif
    #        /* TEMPORARY AND NASTY HACK UNTIL mxSPARSE_CLASS IS COMPLETELY ELIMINATED */
    #        mxSPARSE_CLASS = mxVOID_CLASS /* OBSOLETE! DO NOT USE */
    #        }
    else:
        matlab_type = c_int(5) #VOID_CLASS
    #MxClassID;
    return matlab_type
