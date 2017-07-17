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


    matlab.eval("c = {1, 2, 3; 'text', eye(2,3), {11; 22; 33}}")

    print(matlab.get('c'))


    matlab.put('a', np.array([[1,'asdf'], [3, np.array([1,2,3],dtype='O')]], dtype='O'))
    matlab.eval('a')
    print(matlab.output_buffer)


if __name__ == "__main__":
    main()
