Frequency Asked Questions
=========================


Error: Unknown MATLAB location?
-------------------------------

*matlab_wrapper* is unable to locate your MATLAB installation.

TODO: explain how to fix it



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
