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
def matlab():
    matlab = matlab_wrapper.MatlabSession(
        options='-nojvm',
        buffer_size=1024
    )
    return matlab



def test_eval_ok(matlab):
    command = "a = ones(10)"
    matlab.eval(command)



def test_eval_error(matlab):
    command = "a = onesBLA(10)"

    with pytest.raises(RuntimeError):
        matlab.eval(command)


def test_clear(matlab):
    command = "clear all"
    matlab.eval(command)


def test_longscript(matlab):
    command = """
    for i=1:10
    sprintf('aoeu %i',i);
    end
    """
    matlab.eval(command)


def test_get_numeric(matlab):
    for dtype in NUMERIC_DTYPES:

        a = np.eye(4,5, dtype=dtype)
        matlab.eval("b = eye(4,5, '{}')".format(dtype))
        b = matlab.get('b')

        assert_equal(a.dtype, b.dtype)
        assert_equal(a, b)


def test_get_logical(matlab):
    a = np.eye(4,5, dtype='bool')
    matlab.eval("b = eye(4,5) > 0")
    b = matlab.get('b')

    assert_equal(a.dtype, b.dtype)
    assert_equal(a, b)


def test_get_comples(matlab):
    for dtype in ('single', 'double'):
        a = np.eye(4,5, dtype=dtype) + np.eye(4,5, dtype=dtype)*1j
        matlab.eval("b = eye(4,5, '{0}') + eye(4,5, '{0}')*j".format(dtype))
        b = matlab.get('b')

        assert_equal(a.dtype, b.dtype)
        assert_equal(a, b)


def test_get_string(matlab):
    matlab.eval("s = 'asdf'")
    s = matlab.get('s')

    assert_equal(s, 'asdf')


def test_get_float(matlab):
    matlab.eval("a = 1.")
    a = matlab.get('a')

    assert_equal(a, 1.)



def test_put_numeric(matlab):
    for dtype in NUMERIC_DTYPES:
        a = np.random.randn(2,3) * 10
        a = a.astype(dtype)

        matlab.put('a', a)
        matlab.eval('a')

        output = matlab.output_buffer

        numbers = output.split()[-6:]
        numbers = np.array(numbers, dtype=dtype)
        numbers.shape = (2,3)

        assert_almost_equal(a, numbers, decimal=4)


def test_put_logical(matlab):
    a = np.random.randn(2,3)>0

    matlab.put('a', a)
    matlab.eval('a')

    output = matlab.output_buffer

    numbers = output.split()[-6:]
    numbers = np.array(numbers, dtype=int).astype('bool')
    numbers.shape = (2,3)

    assert_equal(a, numbers)



@pytest.mark.xfail
def test_put_complex(matlab):
    """TODO: fix the test (problem with parsing of the output buffer)"""
    for dtype in ('complex128', 'complex64'):
        a = np.random.randn(2,3)*10 + np.random.randn(2,3)*10j
        a = a.astype(dtype)

        matlab.put('a', a)
        matlab.eval('a')

        output = matlab.output_buffer.split()
        print(output)
        numbers = output[-6:]
        print(numbers)
        numbers = np.array(numbers, dtype=dtype)
        numbers.shape = (2,3)

        assert_almost_equal(a, numbers, decimal=4)



def test_put_string(matlab):
    matlab.put('s', "asdf")
    matlab.eval('s')

    output = matlab.output_buffer.split()

    s = output[-1]

    assert_equal(s, "asdf")




def test_put_float(matlab):
    matlab.put('a', 3.2)
    matlab.eval('a')

    output = matlab.output_buffer.split()

    a = float(output[-1])

    assert_equal(a, 3.2)




def test_put_get_numeric(matlab):
    for dtype in NUMERIC_DTYPES:
        a = np.random.randn(3,2,4) * 10
        a = a.astype(dtype)

        matlab.put('a', a)
        aa = matlab.get('a')

        assert_equal(a.dtype, aa.dtype)
        assert_equal(a, aa)



def test_put_get_logical(matlab):
    a = np.random.randn(3,2,4)>0

    matlab.put('a', a)
    aa = matlab.get('a')

    assert_equal(a.dtype, aa.dtype)
    assert_equal(a, aa)


def test_put_get_complex(matlab):
    for datatype in ("complex64", "complex128"):
        a = np.random.randn(2,4,3) + np.random.randn(2,4,3)*1j
        a = a.astype(datatype)

        matlab.put('a',a)
        aa = matlab.get('a')

        assert_equal(a.dtype, aa.dtype)
        assert_equal(a, aa)



def test_put_get_string(matlab):
    s = "test string\n one more string"

    matlab.put('s', s)
    ss = matlab.get('s')

    assert_equal(s, ss)



def test_workspace_func(matlab):

    x = np.arange(10, dtype=float)
    y = np.sin(x)

    ymatlab = matlab.workspace.sin(x)

    assert_equal(y, ymatlab)



def test_workspace_nout(matlab):
    a = np.array([2,1,3])

    y,i = matlab.workspace.sort(a, nout=2)

    assert_equal(y, [1,2,3])
    assert_equal(i, a)


def test_workspace_pi(matlab):

    pi = matlab.workspace.pi()

    assert_equal(pi, np.pi)


def test_workspace_set_get(matlab):

    matlab.workspace.a = 12.

    matlab.eval("b = a*2")

    b = matlab.workspace.b

    assert_equal(b, 24)


def test_get_cell(matlab):

    matlab.eval("c = {1, 2, 3; 'text', eye(2,3), {11; 22; 33}}")
    actual = matlab.workspace.c

    target = np.array(
        [
            [1., 2., 3.],
            ['text', np.eye(2,3), np.array([11.,22.,33.], dtype='O')]
        ],
        dtype='O'
    )

    assert_equal(actual.shape, target.shape)
    assert_equal(actual.dtype, target.dtype)

    for a,t in zip(actual.flatten(),target.flatten()):
        assert_equal(a,t)


@pytest.mark.xfail
def test_put_cell(matlab):
    # TODO: implement the test
    raise NotImplementedError


def test_put_get_cell(matlab):

    a = np.array(
        [
            [1., 2., 3.],
            ['text', np.eye(2,3), np.array([11.,22.,33.], dtype='O')]
        ],
        dtype='O'
    )

    matlab.workspace.a = a
    aa = matlab.workspace.a

    for el,elel in zip(a.flatten(),aa.flatten()):
        assert_equal(el,elel)
