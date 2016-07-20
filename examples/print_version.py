# -*- coding: utf-8 -*-

"""This demo prints MATLAB version.

"""

from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals

import matlab_wrapper


def main():

    matlab = matlab_wrapper.MatlabSession()

    print("matlab.version:", matlab.version)

    print("raw version string from MATLAB workspace:", matlab.workspace.version())


if __name__ == "__main__":
    main()
