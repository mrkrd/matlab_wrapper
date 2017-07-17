#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Keep putting and getting a variable to MATLAB's workspace.

"""

from __future__ import division, absolute_import, print_function

import numpy as np

import matlab_wrapper
import psutil


def main():
    matlab = matlab_wrapper.MatlabSession()

    p = psutil.Process()

    i = 0
    while True:
        print(i, p.memory_percent(), p.memory_info())

        a = np.random.randn(1e7)

        matlab.put('a', a)
        matlab.get('a')

        i += 1


if __name__ == "__main__":
    main()
