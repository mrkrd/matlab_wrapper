matlab_wrapper
==============

*MATLAB wrapper for Python*


:Name: matlab_wrapper
:Author: Marek Rudnicki
:Email: marekrud@gmail.com
:URL: https://github.com/mrkrd/matlab_wrapper
:License: GNU General Public License v3 or later (GPLv3+)



Description
-----------

*matlab_wrapper* allows you to use MATLAB in an convenient way from
your Python scripts and interactive shell.  MATLAB session is started
in the background and appears as a regular Python module.

*matlab_wrapper* talks to `MATLAB engine library`_ using ctypes_, so
you do not have to compile anything!


.. _`MATLAB engine library`: http://www.mathworks.com/help/matlab/matlab_external/introducing-matlab-engine.html
.. _ctypes: https://docs.python.org/2/library/ctypes.html




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



Requirements
------------

- Python (2.7)
- Matlab (tested with 2013b)
- Numpy (1.8)



Platforms
---------

- GNU/Linux (working, well supported)
- Windows (working, supported)
- OSX (unknown)

Note: I have tested only 64-bit systems.  If you are interested in
32-bit version, please contact me per email or open an issue on
GitHub.

The library should work on OSX with just small changes.
Unfortunately, I have no way to test it.  If you would like support
for OSX, please contact me.



Installation
------------

::

   pip install matlab_wrapper




Issues and Bugs
---------------

https://github.com/mrkrd/matlab_wrapper/issues



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
  - nice ipython notebook support (good)


.. _mlabwrap: http://mlabwrap.sourceforge.net/
.. _mlab: https://github.com/ewiger/mlab
.. _pymatbridge: https://github.com/arokem/python-matlab-bridge


Acknowledgments
---------------

*matlab_wrapper* was forked from pymatlab_.

.. _pymatlab: http://pymatlab.sourceforge.net/
