#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Very simple matlab_wrapper example.

"""

from __future__ import division, absolute_import, print_function

__author__ = "Marek Rudnicki"

import numpy as np

import matlab_wrapper

def main():


    matlab = matlab_wrapper.MatlabSession(
        options='-nojvm',
        buffer_size=1000,
    )


    matlab.eval('a = pi * i')
    a = matlab.get('a')
    print(a)

    matlab.eval("s = 'asdf'")
    s = matlab.get('s')
    print(s)



    matlab.eval("l = logical([1 1 0])")
    l = matlab.get('l')
    print(l)

    print(matlab.output_buffer)

    matlab.put('m', 'asdf')
    m = matlab.get('m')
    print(m)


    # matlab.put('m', np.array('asdf'))
    # m = matlab.get('m')
    # print(m)


    # r = np.arange(9) + np.ones(9) * 1j
    # while True:
    #     matlab.put('r', r)
    #     out = matlab.get('r')
    #     print(out)


if __name__ == "__main__":
    main()
