matlab_wrapper -- history of user-visible changes
=================================================

Changes in version 1
--------------------

+ Switch to int versioning


Changes in version 0.9.8
------------------------

+ Fix a problem with cells (#19)


Changes in version 0.9.7
------------------------

+ Check if Python and MATLAB architectures match


Changes in version 0.9.6
------------------------

+ FIX: proper handling of empty struct arrays (thanks to Jeremy Moreau)


Changes in version 0.9.5
------------------------

+ enable 32-bit versions (thanks to Ralili)
+ disable MATLAB version checking


Changes in version 0.9.4
------------------------

+ Better handling of unsupported Python types
+ matlab.version is tuple now (was string)
+ FIX: platform checking
+ Check for /bin/csh on GNU/Linux


Changes in version 0.9.3
------------------------

+ FIX: memory leaks


Changes in version 0.9
----------------------

+ Initial OS X support (thanks to grahamj1978)


Changes in version 0.8
----------------------

+ Pandas' Series and DataFrame support (put)
+ MATLAB/OS version check and warning
+ BTC donations


Changes in version 0.7.1
------------------------

+ FIX: MatlabSession was ignoring ``matlab_root`` argument


Changes in version 0.7
----------------------

+ Windows support


Changes in version 0.6
----------------------

+ MATLAB struct array support
+ String array support


Changes in version 0.5
----------------------

+ MATLAB cell-array support


Changes in version 0.4 and before
---------------------------------

+ Basic numerical array support
+ Unit tests
+ Easy workspace access
