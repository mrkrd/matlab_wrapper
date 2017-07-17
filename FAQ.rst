Frequency Asked Questions
=========================


Error: Unknown MATLAB location?
-------------------------------

*matlab_wrapper* is unable to locate your MATLAB installation.

There are several ways to fix it:

1. Include a path to the matlab executable in your PATH environment
   variable.  You should be able to type ``matlab`` in your terminal
   prompt and start MATLAB.  *matlab_wrapper* will try to locate the
   libraries based on the location of the ``matlab`` executable file.
   For example, put in your start-up files (.profile)::

     export PATH=$PATH:/opt/MATLAB_R2014a/bin

2. Set the environment variable MATLABROOT to the main MALTAB
   directory, which can be found in MATLAB by typing::

     matlabroot

   Next, type in the shell or your profile file::

     MATLABROOT=/opt/MATLAB/R2014b

3. You can also set MATLAB's root directory in the ``MatlabSession``
   constructor.  The disadvantage is that your script will not be
   portable, e.g.::

     matlab = matlab_wrapper.MatlabSession(matlab_root="/opt/MATLAB/R2014b")

   See the documentation of ``MatlabSession`` for more details.



Error using save, Can't write file stdio?
-----------------------------------------

If you see this error message, is probably due to bug in
``engGetVariable`` in certain versions of MATLAB (2014a, 8.3) on
GNU/Linux and OS X.  There is not much we can do about it.  The
workaround is to use only double arrays.  They seem to be working
properly.



Warning about missing ``/bin/csh``?
-----------------------------------

On some systems MATLAB engine requires ``/bin/csh`` binary and you
have to install it before using *matlab_wrapper*.  For example, on
Debian based distributions such as Ubuntu, you can do it with the
following command as root::

  apt-get install csh

Alternatively, use your favorite package management software.
Additionally, ``tcsh`` package seem to install ``/bin/csh`` too.



Which platforms are supported?
------------------------------

GNU/Linux, Windows, OS X and various versions of MATLAB.

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



Is there alternative software?
------------------------------

Yes.  Here's a little compilation:

(last updated on April 18, 2015)


- `MATLAB Engine for Python`_

  - official package from Mathworks
  - supports new versions of Python (2.7, 3.3, and 3.4)
  - ships with MATLAB 2015a

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
  - nice IPython Notebook support (good)



There is a nice overview of the `available packages`_ at
StackOverflow.


.. _`MATLAB Engine for Python`: http://mathworks.com/help/matlab/matlab-engine-for-python.html
.. _pymatlab: http://pymatlab.sourceforge.net/
.. _mlabwrap: http://mlabwrap.sourceforge.net/
.. _mlab: https://github.com/ewiger/mlab
.. _pymatbridge: https://github.com/arokem/python-matlab-bridge
.. _`available packages`: https://stackoverflow.com/questions/2883189/calling-matlab-functions-from-python/23762412#23762412
