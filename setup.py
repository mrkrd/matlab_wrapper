#!/usr/bin/python

from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

setup(
    name="matlab_wrapper",
    version="1",
    author="Marek Rudnicki",
    author_email="marekrud@posteo.de",

    description="MATLAB wrapper for Python",
    license="GPLv3",
    url="https://github.com/mrkrd/matlab_wrapper",
    download_url="https://github.com/mrkrd/matlab_wrapper/tarball/master",

    packages=find_packages(),
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],

    platforms=["Linux", "Windows", "OSX"],
    install_requires=["numpy"],
)
