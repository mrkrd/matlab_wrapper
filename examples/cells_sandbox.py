#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing things with cells.

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


    matlab.eval("c = {1, 2, 3; 'text', rand(5,10,2), {11; 22; 33}}")

    print(matlab.get('c'))


if __name__ == "__main__":
    main()
