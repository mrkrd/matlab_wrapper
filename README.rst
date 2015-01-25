matlab_wrapper
==============


*matlab_wrapper* allows you to use MATLAB directly from your Python
scripts and an interactive shell.  MATLAB session is started in the
background and appears as a regular Python module.

:Homepage: https://github.com/mrkrd/matlab_wrapper
:Documentation: https://pythonhosted.org/matlab_wrapper/


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
.. _NEWS: NEWS.rst



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

First, check our guidelines in CONTRIBUTING.rst_ file.

- Issue Tracker: https://github.com/mrkrd/matlab_wrapper/issues
- Source Code: https://github.com/mrkrd/matlab_wrapper

.. _CONTRIBUTING.rst: CONTRIBUTING.rst


Support
-------

If you are having issues, please let us know either by:

- opening a new issue: https://github.com/mrkrd/matlab_wrapper/issues
- per email: Marek Rudnicki <marekrud@gmail.com>

Before reporting an issue, check FAQ_ and CONTRIBUTING_.

.. _FAQ: FAQ.rst
.. _CONTRIBUTING: CONTRIBUTING.rst



Alternatives
------------

(last updated on June 17, 2014)

- pymatlab_

  - pure Python, no compilation, using ctypes (good)
  - quite raw (ugly)
  - memory leaks (bad)

- mlabwrap_

  - cool interface, mlab.sin() (good)
  - needs compilation (bad)
  - not much development (bad)

- mlab_

  - similar interface to mlabwrap (good)
  - using raw pipes (hmm)
  - there is another very old package with `the same name
    <http://claymore.engineer.gvsu.edu/~steriana/Python/pymat.html>`_
    (ugly)

- pymatbridge_

  - actively developed (good)
  - client-server architecture with ZeroMQ and JSON, complex (ugly)
  - missing basic functions, there's no ``put`` (bad)
  - nice IPython Notebook support (good)



There is a nice overview of the `available packages`_ at
StackOverflow.


.. _mlabwrap: http://mlabwrap.sourceforge.net/
.. _mlab: https://github.com/ewiger/mlab
.. _pymatbridge: https://github.com/arokem/python-matlab-bridge
.. _`available packages`: https://stackoverflow.com/questions/2883189/calling-matlab-functions-from-python/23762412#23762412



Acknowledgments
---------------

*matlab_wrapper* was forked from pymatlab_.

MATLAB is a registered trademark of `The MathWorks, Inc`_.

.. _pymatlab: http://pymatlab.sourceforge.net/
.. _`The MathWorks, Inc`: http://www.mathworks.com/



License
-------

The project is licensed under the `GNU General Public License v3`_ or
later (GPLv3+).

.. _`GNU General Public License v3`: COPYING.txt
