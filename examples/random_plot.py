#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Let's plot something random in MATLAB.

"""

from __future__ import division, absolute_import, print_function

import numpy as np

import matlab_wrapper

def main():
    matlab = matlab_wrapper.MatlabSession()

    x = np.random.randn(100)

    matlab.workspace.plot(x)

    raw_input("Press enter to finish...")


if __name__ == "__main__":
    main()
