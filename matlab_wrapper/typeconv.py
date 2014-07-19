# -*- coding: utf-8 -*-

# Copyright 2010-2013 Joakim Möller
# Copyright 2014 Marek Rudnicki
#
# This file is part of matlab_wrapper.
#
# matlab_wrapper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# matlab_wrapper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with matlab_wrapper.  If not, see <http://www.gnu.org/licenses/>.


from ctypes import *
from numpy import array,ndarray,dtype
from os.path import join
import platform
import sys,numpy


def dtype_to_mat(dtype):

    #Typedef enum
    #{
    #0        mxUNKNOWN_CLASS = 0,
    #1        mxCELL_CLASS,
    #2        mxSTRUCT_CLASS,
    #3        mxLOGICAL_CLASS,
    if dtype.type == numpy.bool_:
        matlab_type = c_int(3)
    #4        mxCHAR_CLASS,
    elif dtype.type == numpy.str_:
        matlab_type = c_int(4)
    #5        mxVOID_CLASS,
    elif dtype.type == numpy.void:
        matlab_type = c_int(5)
    #6        mxDOUBLE_CLASS,
    elif dtype.type == numpy.complex128:
        matlab_type = c_int(6)
    elif dtype.type == numpy.float64:
        matlab_type = c_int(6)
    #7        mxSINGLE_CLASS,
    elif dtype.type ==numpy.complex64:
        matlab_type = c_int(7)
    elif dtype.type ==numpy.float32:
        matlab_type = c_int(7)
    #8        mxINT8_CLASS,
    elif dtype.type ==numpy.int8:
        matlab_type = c_int(8)
    #9        mxUINT8_CLASS,
    elif dtype.type ==numpy.uint8:
        matlab_type = c_int(9)
    #10       mxINT16_CLASS,
    elif dtype.type ==numpy.int16:
        matlab_type = c_int(10)
    #11       mxUINT16_CLASS,
    elif dtype.type ==numpy.uint16:
        matlab_type = c_int(11)
    #12       mxINT32_CLASS,
    elif dtype.type ==numpy.int32:
        matlab_type = c_int(12)
    #13       mxUINT32_CLASS,
    elif dtype.type ==numpy.uint32:
        matlab_type = c_int(13)
    #14       mxINT64_CLASS,
    elif dtype.type ==numpy.int64:
        matlab_type = c_int(14)
    #15       mxUINT64_CLASS,
    elif dtype.type ==numpy.uint64:
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
