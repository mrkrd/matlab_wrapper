matlab_wrapper
==============

MATLAB wrapper for Python


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

- pymatlab
- mlabwrap
- mlab



Acknowledgments
---------------

matlab_wrapper was forked from pymatlab_.

.. _pymatlab: http://pymatlab.sourceforge.net/
