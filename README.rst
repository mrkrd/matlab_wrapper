=====================================
Python interface to MATLAB (pymatlab)
=====================================

This package lets Python users interface and communicate with MATLAB from
Python. Pymatlab makes it easier for users to integrate a project with a large
MATLAB codebase into python scripts by using MATLAB scripts as a part of the
python program.

The basic functionality of this package is to send data from Python to MATLAB's
workspace to be able to run Matlab function on the data. After processing you
retrieve back data to python. This enables you to process data with Mathlab's
built in functions, toolboxes or Matlab-scripts. It is also possible to use
MATLAB's to generate plots or other graphics.

The package uses Numpy's ndarrays and translates them into MATLAB's mxarrays
using Python's ctypes and Matlab's mx library. The interface to MATLAB's
workspace in done through MATLAB's engine library.


Download
--------

Downloading is possible from PyPi_ and `SourceForge pymatlab files`__. Since
pymatlab is hosted at SourceForge_ the latest development version is available
from git. There are different branches available this is the ctypes variant.

.. _PyPi: http://pypi.python.org  
.. _Files: http://sourceforge.net/projects/pymatlab/files/
.. _SourceForge: http://sourceforge.net

__ Files_

Installing
----------

Standard installation method using pip, easy_install or 'python setup.py
install'.

Preparing to use pymatlab
-------------------------

You need MATLAB_ from Mathworks properly installed on your local machine.

.. _MATLAB: http://www.mathworks.se/products/matlab/ 

Linux:

C-shell has to be installed in order to make the Matlab connection work. Also
the path to the matlab binary needs to be set.

 $ sudo apt-get install csh
 $ export PATH = /opt/MATLAB/R2013a/bin:$PATH

Win:

On Windows make sure the Matlab DLLs are in your "Path" environment variable.
This version is not tested in Windows but should be possible to run with some
debugging efforts.

Requirements
------------

- Python

    Version 2.
 
- Matlab 
    
    Versions 2009a,2010a,2013a tested. Presumably any version?

- Numpy

    Any version? tested on version 1.3.0. 

Limitations
-----------

The current version lets you transfer arrays of any rank between Python and
Matlab using the following datatypes: Single and double precision floatpoint
numbers. Integer numbers of different bit lengths (8-64) unsigned or signed.
Complex numbers (single or double precision). Logical arrays. Any other types
will probably fail or give unpredictable results.

Using pymatlab
--------------

First import:

>>> import pymatlab
    
Initialise the interpretor.

>>> session = pymatlab.session_factory()

Create an numpy-array to start the work.

>>> from numpy.random import randn
>>> a = randn(20,10,30)

Send the numpy array a to the MATLAB Workspace to the variable 'A'
  
>>> session.putvalue('A',a)

Do something in matlab in MATLAB with variable A. Sucessfull commands return
an empty string - if MATLAB generates an error the returning string holds the
error message
    
>>> session.run('B=2*A')

>>> session.run('C')
Traceback (most recent call last):
    ...
RuntimeError: Error from Matlab: Error: MATLAB:UndefinedFunction with message: Undefined function or variable 'C'.
<BLANKLINE>

A trick to make larger scripts more failsafe with regards to syntax errors.
Send a script to a string variable and run it with eval().

>>> mscript = """D = A
... for i=1:10
...    D = 2*D
... end
... """
>>> session.putvalue('MSCRIPT',mscript)
>>> session.run('eval(MSCRIPT)')

To retrive the variable back to python:

>>> b = session.getvalue('B')
>>> (2*a==b).all()
True


If you want to explicitly close the connection to the interpreter delete the
instance. Normally Matlab will be close when the session variable runs out of
scope.

>>> del session

Bugs, support and feature requests
----------------------------------

All bug reports, feature requests or support questions are directed
to to pymatlab@molflow.com.

Please  consider to support us in our efforts by `donating to pymatlab`__. Your
donations will be used to buy hardware and software licenses to be able to
continue to develop this package. 

.. _Donations: http://sourceforge.net/donate/index.php?group_id=307148

__ Donations_
