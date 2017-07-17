#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Very simple matlab_wrapper example.

"""

from __future__ import division, absolute_import, print_function

import numpy as np

import matlab_wrapper

def main():


    matlab = matlab_wrapper.MatlabSession(
        options='-nojvm',
        buffer_size=1000,
    )

    print(matlab.version)


    print()
    print('='*70)
    print()


    matlab.eval("a = pi * 2")
    print(matlab.output_buffer)
    a = matlab.get('a')
    print(a)


    print()
    print('='*70)
    print()



    matlab.eval("s = 'asdf'")
    s = matlab.get('s')
    print(s)



    print()
    print('='*70)
    print()



    matlab.eval("l = logical([1 1 0])")
    l = matlab.get('l')
    print(l)

    print(matlab.output_buffer)



    print()
    print('='*70)
    print()


    matlab.put('m', 'asdf')
    m = matlab.get('m')
    print(m)



    print()
    print('='*70)
    print()


    # matlab.put('m', np.array('asdf'))
    # m = matlab.get('m')
    # print(m)


    # r = np.arange(9) + np.ones(9) * 1j
    # while True:
    #     matlab.put('r', r)
    #     out = matlab.get('r')
    #     print(out)


    a = matlab.workspace.sin(np.arange(10.))
    print(a)


    print()
    print('='*70)
    print()


    y,i = matlab.workspace.sort([2,1,3], nout=2)
    print(y,i)


    print()
    print('='*70)
    print()


    print(matlab.workspace.pi())


    print()
    print('='*70)
    print()

    matlab.workspace.a = [123, 12, 1]
    matlab.eval("b = a*2")
    print(matlab.workspace.b)

    #help(matlab.workspace.sin)


    print()
    print('='*70)
    print()


    matlab.eval("whos")
    print(matlab.output_buffer)


    print()
    print('='*70)
    print()


    print(matlab)


    print()
    print('='*70)
    print()


    matlab.workspace.a = ['asdf', 'strings']

    matlab.eval('a')
    print(matlab.output_buffer)


if __name__ == "__main__":
    main()
