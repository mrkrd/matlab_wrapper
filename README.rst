matlab_wrapper
==============


*matlab_wrapper* allows you to use MATLAB directly from your Python
scripts and an interactive shell.  MATLAB session is started in the
background and appears as a regular Python module.



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




Platforms
---------

If you are using *matlab_wrapper* with MATLAB version or OS, which are
not listed below, please let us know and we will update the table.

==========  ===========  ==========  ==========
OS [#os]_   MATLAB       Bits [#b]_  Status
==========  ===========  ==========  ==========
GNU/Linux   2014b (8.4)  64          working (py.test OK)
GNU/Linux   2014a (8.3)  64          only double arrays working [#f]_
GNU/Linux   2013b (8.2)  64          working (py.test OK)
GNU/Linux   2013a (8.1)  64          working (py.test OK)

Windows     2014b (8.4)  32          reported working
Windows     2014a (8.3)  64          working (py.test OK)

OS X        2014a (8.3)  64          only double arrays working [#f]_
OS X        2013a (8.1)  64          working
==========  ===========  ==========  ==========


.. [#os] OSX version should work, but I'm unable to test it.  If you
         have problems, let me know and we might figure it out.

.. [#b] We have tested only 64-bit systems.  32-bit architectures are
        enabled, but not well tested.

.. [#f] Due to bug in ``engGetVariable``: Error using save, Can't
        write file stdio.



Contribute
----------

- Issue Tracker: https://github.com/mrkrd/matlab_wrapper/issues
- Source Code: https://github.com/mrkrd/matlab_wrapper




Support
-------

If you are having issues, please let us know by either:

- opening a new issue: https://github.com/mrkrd/matlab_wrapper/issues
- per email: Marek Rudnicki <marekrud@gmail.com>

When reporting problems, specify which Python (version, architecture,
distribution), MATLAB (version, architecture) and OS (version,
architecture) are you using.




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
