#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing things with cells.

"""

from __future__ import division, absolute_import, print_function

import numpy as np

import matlab_wrapper

def main():

    matlab = matlab_wrapper.MatlabSession(
        options='-nojvm',
        buffer_size=1000,
    )


    matlab.eval("""
    s = struct()

    s(1,1).x = 1
    s(1,1).y = 'a'

    s(2,2).x = 2
    s(2,2).y = [1,2,3]

    """)

    print(matlab.get('s'))


    matlab.eval("""
    s = struct()

    s(1).x = 1
    s(1).y = [1 2]

    s(2).x = 2
    s(2).y = [3 5]
    """)

    s = matlab.get('s')
    print(s, s.dtype)

    print("="*70)

    a = np.array([(1,'a'), (2,'b')], dtype=[('x', '<i8'), ('y', 'S1')])

    matlab.put('a', a)

    matlab.eval('a\n a(1)\n a(2)')
    print(matlab.output_buffer)


if __name__ == "__main__":
    main()
