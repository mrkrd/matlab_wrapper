Contributing Guidelines
=======================



Reporting Issues
----------------

- Make sure that the issue is not addressed in the FAQ_.

- Provide information about your setup:

  - Python (version, architecture, distribution)
  - MATLAB (version, architecture)
  - OS (version, architecture)

- Describe how to reproduce the issue and copy-paste the error
  messages in the report.

- At best, provide a small code snippet, that can run by itself and
  illustrates the problem.



.. _FAQ: https://pythonhosted.org/matlab_wrapper/faq.html





Contributing new Code
---------------------

- Source code is located at: https://github.com/mrkrd/matlab_wrapper

- Patches or pull requests are very welcome!

- Good place to start is the TODO.org_ file (best viewd in Emacs
  org-mode).  At the moment, all new features and ideas go through
  this file.  The status of the item can be: DONE (already
  implemented), TODO (some work has been started) or no status (not
  started).  The items often contain some intended implementation
  details and remarks.  You can also contact me per email_ for further
  details.

- Coding style is mostly PEP8 compliant and The Zen of Python is your
  friend::

    >>> import this

- Module installation in the developer mode can be useful::

    python setup.py develop --user

- Each new feature should have a test case in the tests directory.
  Make sure that tests are passing using py.test_.

- Add your name to AUTHORS.rst_ file.


.. _GitHub: https://github.com/mrkrd/matlab_wrapper
.. _TODO.org: https://raw.githubusercontent.com/mrkrd/matlab_wrapper/master/TODO.org
.. _email: marekrud@gmail.com
.. _py.test: http://pytest.org
.. _AUTHORS.rst: https://github.com/mrkrd/matlab_wrapper/blob/master/AUTHORS.rst
