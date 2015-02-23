# -*- coding: utf-8 -*-

"""Evaluate m-file and collect the results.

"""
from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals

__author__ = "Marek Rudnicki"
__copyright__ = "Copyright 2014, Marek Rudnicki"
__license__ = "GPLv3+"


import matlab_wrapper


def main():
    matlab = matlab_wrapper.MatlabSession()

    matlab.put('x', 2.)
    matlab.eval('my_script')
    y = matlab.get('y')

    print("And the winner is:", y)


if __name__ == "__main__":
    main()
