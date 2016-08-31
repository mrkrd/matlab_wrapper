Contributing Guidelines
=======================



Reporting Issues
----------------

- Make sure that the issue is not addressed in the FAQ.rst_ file.

- Provide information about your setup:

  - Python (version, architecture, distribution)
  - MATLAB (version, architecture)
  - OS (version, architecture)

- Describe how to reproduce the issue and copy-paste the error
  messages in the report.

- At best, provide a small code snippet, that can run by itself and
  illustrates the problem.

- Use the `issue tracker`_.


.. _FAQ.rst: FAQ.rst
.. _issue tracker: https://github.com/mrkrd/matlab_wrapper/issues




Contributing new Code
---------------------

- Source code is located at: https://github.com/mrkrd/matlab_wrapper

- Your patches or pull requests are very welcome!

- Good place to start is the TODO.org_ file (best viewd in Emacs
  org-mode).  At the moment, all new features and ideas go through
  this file.  The status of the item can be: DONE (already
  implemented), TODO (some work has been started) or no status (not
  started).  The items often contain some intended implementation
  details and remarks.  You can also request more details through our
  issue tracker.

- Coding style is mostly PEP8 compliant and The Zen of Python is your
  friend::

    >>> import this

- Module installation in the developer mode can be useful::

    python setup.py develop --user

- Each new feature should have a test case in the tests directory.
  Make sure that tests are passing using py.test_.

- Add your name to AUTHORS.rst_ file.


.. _TODO.org: TODO.org
.. _py.test: http://pytest.org
.. _AUTHORS.rst: AUTHORS.rst
