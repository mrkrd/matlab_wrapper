# -*- coding: utf-8 -*-

"""Design a lowpas FIR filter.  Based on an example from `freqz`
documentation.

"""

from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals

import numpy as np
import matlab_wrapper


def main():

    matlab = matlab_wrapper.MatlabSession()

    kaiser = matlab.workspace.kaiser(81., 8.)

    b = matlab.workspace.fir1(80., 0.5, kaiser)

    matlab.workspace.freqz(b, 1., nout=0)

    raw_input("Press enter to finish...")


if __name__ == "__main__":
    main()
