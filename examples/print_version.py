# -*- coding: utf-8 -*-

"""This demo prints MATLAB version.

"""

from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals

__author__ = "Marek Rudnicki"
__copyright__ = "Copyright 2014, Marek Rudnicki"
__license__ = "GPLv3+"


import matlab_wrapper


def main():

    matlab = matlab_wrapper.MatlabSession()

    print("matlab.version:", matlab.version)

    print("raw version string from MATLAB workspace:", matlab.workspace.version())


if __name__ == "__main__":
    main()
