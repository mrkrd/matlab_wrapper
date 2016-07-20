#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Keep restarting MATLAB.

"""

from __future__ import division, absolute_import, print_function

import matlab_wrapper
import psutil


def main():

    p = psutil.Process()

    i = 0
    while True:
        print(i, p.memory_percent(), p.memory_info())

        matlab = matlab_wrapper.MatlabSession()

        i += 1


if __name__ == "__main__":
    main()
