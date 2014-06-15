#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test MatlabSession

"""

from __future__ import division, absolute_import, print_function

__author__ = "Marek Rudnicki"

import numpy as np
from numpy.testing import assert_equal, assert_almost_equal

import matlab_wrapper

import pytest


NUMERIC_DTYPES = ('int8', 'int16', 'int32', 'int64', 'uint8',
                  'uint16', 'uint32', 'uint64', 'single', 'double')


np.random.seed(0)


@pytest.fixture(scope='module')
def session():
    session = matlab_wrapper.MatlabSession(
        options='-nojvm',
        buffer_size=1024
    )
    return session



def test_eval_ok(session):
    command = "a = ones(10)"
    session.eval(command)



def test_eval_error(session):
    command = "a = onesBLA(10)"

    with pytest.raises(RuntimeError):
        session.eval(command)


def test_clear(session):
    command = "clear all"
    session.eval(command)


def test_longscript(session):
    command = """
    for i=1:10
    sprintf('aoeu %i',i);
    end
    """
    session.eval(command)


def test_get_numeric(session):
    for dtype in NUMERIC_DTYPES:

        a = np.eye(4,5, dtype=dtype)
        session.eval("b = eye(4,5, '{}')".format(dtype))
        b = session.get('b')

        assert a.dtype == b.dtype
        assert_equal(a, b)


def test_get_logical(session):
    a = np.eye(4,5, dtype='bool')
    session.eval("b = eye(4,5) > 0")
    b = session.get('b')

    assert a.dtype == b.dtype
    assert_equal(a, b)


def test_get_comples(session):
    for dtype in ('single', 'double'):
        a = np.eye(4,5, dtype=dtype) + np.eye(4,5, dtype=dtype)*1j
        session.eval("b = eye(4,5, '{0}') + eye(4,5, '{0}')*j".format(dtype))
        b = session.get('b')

        assert a.dtype == b.dtype
        assert_equal(a, b)


def test_get_string(session):
    session.eval("s = 'asdf'")
    s = session.get('s')

    assert s == 'asdf'


def test_get_float(session):
    session.eval("a = 1.")
    a = session.get('a')

    assert a == 1.



def test_put_numeric(session):
    for dtype in NUMERIC_DTYPES:
        a = np.random.randn(2,3) * 10
        a = a.astype(dtype)

        session.put('a', a)
        session.eval('a')

        output = session.output_buffer

        numbers = output.split()[-6:]
        numbers = np.array(numbers, dtype=dtype)
        numbers.shape = (2,3)

        assert_almost_equal(a, numbers, decimal=4)


def test_put_logical(session):
    a = np.random.randn(2,3)>0

    session.put('a', a)
    session.eval('a')

    output = session.output_buffer

    numbers = output.split()[-6:]
    numbers = np.array(numbers, dtype=int).astype('bool')
    numbers.shape = (2,3)

    assert_equal(a, numbers)



@pytest.mark.xfail
def test_put_complex(session):
    """TODO: fix the test (problem with parsing of the output buffer)"""
    for dtype in ('complex128', 'complex64'):
        a = np.random.randn(2,3)*10 + np.random.randn(2,3)*10j
        a = a.astype(dtype)

        session.put('a', a)
        session.eval('a')

        output = session.output_buffer.split()
        print(output)
        numbers = output[-6:]
        print(numbers)
        numbers = np.array(numbers, dtype=dtype)
        numbers.shape = (2,3)

        assert_almost_equal(a, numbers, decimal=4)



def test_put_string(session):
    session.put('s', "asdf")
    session.eval('s')

    output = session.output_buffer.split()

    s = output[-1]

    assert s == "asdf"




def test_put_float(session):
    session.put('a', 3.2)
    session.eval('a')

    output = session.output_buffer.split()

    a = float(output[-1])

    assert a == 3.2




def test_put_get_numeric(session):
    for dtype in NUMERIC_DTYPES:
        a = np.random.randn(3,2,4) * 10
        a = a.astype(dtype)

        session.put('a', a)
        aa = session.get('a')

        assert a.dtype == aa.dtype
        assert_equal(a, aa)



def test_put_get_logical(session):
    a = np.random.randn(3,2,4)>0

    session.put('a', a)
    aa = session.get('a')

    assert a.dtype == aa.dtype
    assert_equal(a, aa)


def test_put_get_complex(session):
    for datatype in ("complex64", "complex128"):
        a = np.random.randn(2,4,3) + np.random.randn(2,4,3)*1j
        a = a.astype(datatype)

        session.put('a',a)
        aa = session.get('a')

        assert a.dtype == aa.dtype
        assert_equal(a, aa)



def test_put_get_string(session):
    s = "test string\n one more string"

    session.put('s', s)
    ss = session.get('s')

    assert s == ss



def test_workspace_func(session):

    x = np.arange(10, dtype=float)
    y = np.sin(x)

    ymatlab = session.workspace.sin(x)

    assert_equal(y, ymatlab)



def test_workspace_nout(session):
    a = np.array([2,1,3])

    y,i = session.workspace.sort(a, nout=2)

    assert_equal(y, [1,2,3])
    assert_equal(i, a)
