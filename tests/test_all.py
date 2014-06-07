import unittest,doctest
from tests import t_matlab

def test_suite():
    return unittest.TestSuite([
        t_matlab.test_suite(),
        doctest.DocFileSuite('../../README.txt'),
        ])
            
