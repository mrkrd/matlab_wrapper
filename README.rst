matlab_wrapper
==============

MATLAB wrapper for Python


Description
-----------

**matlab_wrapper** allows you to use MATLAB in an convenient way from
your Python scripts.  The MATLAB session is started in the background
and appears as a regular Python module.

**matlab_wrapper** uses standard `MATLAB engine library`_ and talks
directly to the binaries through `ctypes module`_. (you do not need to
compile anything!)


.. _`MATLAB engine library`: http://www.mathworks.com/help/matlab/matlab_external/introducing-matlab-engine.html
.. _`ctypes module`: https://docs.python.org/2/library/ctypes.html


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

  matlab.workspace.a = 12.3
  b = matlab.workspace.b



Requirements
------------

- Python (2.7)
- Matlab (tested with 2013b)
- Numpy (1.8)



Installation
------------

::

   pip install matlab_wrapper



Limitations
-----------

- Cells are not yet supported.
- Struct arrays are not yet supported.
- Support on Windows and OSX is not as good as on GNU/Linux (I'm
  looking forward to contributors).



Issues and Bugs
---------------

https://github.com/mrkrd/matlab_wrapper/issues



Alternatives
------------

- pymatlab_
- mlabwrap_
- mlab_
- pymatbridge_

.. _mlabwrap: http://mlabwrap.sourceforge.net/
.. _mlab: https://github.com/ewiger/mlab
.. _pymatbridge: https://github.com/arokem/python-matlab-bridge


Acknowledgments
---------------

matlab_wrapper was forked from pymatlab_.

.. _pymatlab: http://pymatlab.sourceforge.net/
