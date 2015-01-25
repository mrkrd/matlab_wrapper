matlab_wrapper
==============

*matlab_wrapper* allows you to use MATLAB directly from your Python
scripts and an interactive shell.  MATLAB session is started in the
background and appears as a regular Python module.

The documentation is located at
https://pythonhosted.org/matlab_wrapper/.



Usage
-----

Initialize::

  import matlab_wrapper
  matlab = matlab_wrapper.MatlabSession()


Low level::

  matlab.put('a', 12.3)
  matlab.eval('b = a * 2')
  b = matlab.get('b')


Workspace::

  s = matlab.workspace.sin([0.1, 0.2, 0.3])

  sorted,idx = matlab.workspace.sort([3,1,2], nout=2)

  matlab.workspace.a = 12.3
  b = matlab.workspace.b


More examples are in the examples_ directory!

.. _examples: https://github.com/mrkrd/matlab_wrapper/tree/master/examples



Features
--------

- Access MATLAB variables and functions from Python
- Multiplatform: GNU/Linux, Windows, OS X
- On-the-fly conversion between MATLAB and Numpy data types
- Support for MATLAB's numerical, logical, struct and cell arrays
- Pure Python, no need to compile anything (*matlab_wrapper* talks to
  `MATLAB engine library`_ using ctypes_)

For a complete list of changes including new features, check the
NEWS_.

.. _`MATLAB engine library`: http://www.mathworks.com/help/matlab/matlab_external/introducing-matlab-engine.html
.. _ctypes: https://docs.python.org/2/library/ctypes.html
.. _NEWS: https://pythonhosted.org/matlab_wrapper/news.html



Installation
------------

First, make sure that you have the following components installed:

- Python (2.7, no Python 3 support yet)
- MATLAB (various versions)
- Numpy


Next, install *matlab_wrapper* using pip (the standard Python package
installation tool) from your command line::

   pip install matlab_wrapper



Contribute
----------

Check our CONTRIBUTING_ guidelines.

.. _CONTRIBUTING: https://pythonhosted.org/matlab_wrapper/contributing.html



Support
-------

If you are having issues, please let us know either by:

- opening a new issue: https://github.com/mrkrd/matlab_wrapper/issues
- per email: Marek Rudnicki <marekrud@gmail.com>

Before reporting an issue, check FAQ_ and CONTRIBUTING_.

.. _FAQ: https://pythonhosted.org/matlab_wrapper/faq.html
.. _CONTRIBUTING: https://pythonhosted.org/matlab_wrapper/contributing.html



Acknowledgments
---------------

*matlab_wrapper* was forked from pymatlab_.

MATLAB is a registered trademark of `The MathWorks, Inc`_.

.. _pymatlab: http://pymatlab.sourceforge.net/
.. _`The MathWorks, Inc`: http://www.mathworks.com/



License
-------

The project is licensed under the GNU General Public License v3 or
later (GPLv3+).
