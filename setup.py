#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from setuptools import setup,find_packages
from os.path import join
setup(
        name='pymatlab',
        version='0.2.3',
        description = 'A pythonic interface to MATLAB',
        long_description=open("README.txt").read() + "\n" + 
            open(join("docs", "CHANGELOG.txt")).read(),
        packages = find_packages('src'),
        package_dir={'':'src'},
        classifiers=['Development Status :: 3 - Alpha',
                        'Intended Audience :: End Users/Desktop',
                        'Intended Audience :: Developers',
                        'Intended Audience :: Science/Research',
                        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                        'Operating System :: POSIX',
                        'Programming Language :: Python',
                          ],
        test_suite='tests.test_all.test_suite',
        url = 'http://pymatlab.sourceforge.net/',
        author='Joakim Möller',
        author_email='joakim.moller@molflow.com',
        license='GPLv3',
        platforms=['Linux','Windows'],
        install_requires=['setuptools','numpy'],
        download_url=['https://sourceforge.net/projects/pymatlab/files/'],
        #tests_require=['setuptools'],
)

