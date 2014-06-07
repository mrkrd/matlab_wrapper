import unittest
#import mocker


import sys
import pymatlab
import numpy
from numpy import eye,arange,ones,array,ndarray
from numpy.random import randn
from numpy.ma.testutils import assert_equal,assert_almost_equal
from StringIO import StringIO

class MatlabTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = pymatlab.session_factory()
        
    def runOK(self):
        command="A=ones(10);"
        self.session.run(command)

    def runNOK(self):
        command="A=oxes(10);"
        self.assertRaises(RuntimeError,self.session.run,command)

    def clear(self):
        command="clear all"
        self.session.run(command)

    def syntaxerror(self):
        command="""if 1,"""
        self.session.putvalue('test',command)
        self.assertRaises(RuntimeError,self.session.run,'eval(test)')

    def longscript(self):
        command = """for i=1:10
                        sprintf('aoeu %i',i);
                     end"""
        self.session.run(command)

    def getvalue(self):
        for datatype in [
                "int8",
                "int16",
                "int32",
                "int64",
                "uint8",
                "uint16",
                "uint32",
                "uint64",
                "single",
                "double",
                ]:
            a = eye(4,5,dtype=datatype)
            err = self.session.run("b=eye(4,5,'{}')".format(datatype))
            b = self.session.getvalue('b')
            self.assertEqual(a.dtype,b.dtype)
            assert_equal(a,b)

    def getvalue_logical(self):
            a = eye(4,5,dtype='bool')
            err = self.session.run("b=eye(4,5)>0")
            b = self.session.getvalue('b')
            self.assertEqual(a.dtype,b.dtype)
            assert_equal(a,b)

    def getvalue_complex(self):
        for datatype in [
                "single",
                "double",
                ]:
            a = eye(4,5,dtype=datatype) + eye(4,5,dtype=datatype)*1j
            err = self.session.run("b=eye(4,5,'{0}')+eye(4,5,'{0}')*j".format(datatype))
            b = self.session.getvalue('b')
            self.assertEqual(a.dtype,b.dtype)
            assert_equal(a,b)

    def putvalue(self):
        for datatype in [
                "int8",
                "int16",
                "int32",
                "int64",
                "uint8",
                "uint16",
                "uint32",
                "uint64",
                "f",
                "d",
                ]:
            ar = randn(2,3)*10
            a = ar.astype(datatype)
            self.session.putvalue('a',a)
            self.session.run('a')
            buf = self.session.buf.value
            vector = buf.split()
            data = [array(i).astype(datatype) for i in vector[-6:]]
            buf=array(data)
            buf.shape=(2,3)
            assert_almost_equal(a,buf,4)

    def putvalue_logical(self):
            a = randn(2,3)>0
            self.session.putvalue('a',a)
            self.session.run('a')
            buf = self.session.buf.value
            vector = buf.split()
            data = [array(i).astype('bool') for i in vector[-6:]]
            buf=array(data)
            buf.shape=(2,3)
            assert_equal(a,buf)
    def putvalue_complex(self):
        for datatype in [
                "complex128",
                "complex64",
                ]:
            ar = randn(2,3)*10+randn(2,3)*10j
            a = ar.astype(datatype)
            self.session.putvalue('a',a)
            self.session.run('a')
            buf = self.session.buf.value
            vector = buf.split()
            data = [array(i).astype(datatype) for i in vector[-6:]]
            buf=array(data)
            buf.shape=(2,3)
            assert_almost_equal(a,buf,4)

    def getput(self):
        for datatype in [
                "int8",
                "int16",
                "int32",
                "int64",
                "uint8",
                "uint16",
                "uint32",
                "uint64",
                "f",
                "d",
                ]:
            ar = randn(3,2,4)*10
            a = ar.astype(datatype)  
            self.session.putvalue('A',a)
            b = self.session.getvalue('A')
            self.assertEqual(a.dtype,b.dtype)
            assert_equal(a,b)

    def getput_logical(self):
            a = randn(3,2,4)>0
            self.session.putvalue('A',a)
            b = self.session.getvalue('A')
            self.assertEqual(a.dtype,b.dtype)
            assert_equal(a,b)


    def getput_complex(self):
        for datatype in [
                "complex64",
                "complex128",
                ]:
            ar = randn(2,4,3)+randn(2,4,3)*1j
            a = ar.astype(datatype)  
            self.session.putvalue('A',a)
            b = self.session.getvalue('A')
            self.assertEqual(a.dtype,b.dtype)
            assert_equal(a,b)
        

    def getput_string(self):
        a = "test string\n test again"
        self.session.putvalue('A',a)
        self.session.run('display(A)')
        buf = self.session.buf.value
        b = self.session.getvalue('A')
        self.assertEqual(buf.split()[5:],a.split())
        self.assertEqual(a,b)

    def check_order_mult(self):
        a = 1.0 * numpy.array([[1, 4], [2, 5], [3, 6]])
        b = 1.0 * numpy.array([[7, 9, 11, 13], [8, 10, 12, 14]])
        s = self.session
        s.putvalue('A', a)
        s.putvalue('B', b)
        s.run("C = A*B;")
        c = s.getvalue('C')
        assert_equal(c.astype(int), numpy.dot(a, b).astype(int))

    def check_order_vector(self):
        a = 1.0 * numpy.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        s = self.session
        s.putvalue('A', a)
        s.run("B = A(1:9);")
        b = s.getvalue('B')
        assert_equal(b.astype(int), numpy.array(range(1, 10)).astype(int))

def test_suite():
    # Want to run them in a certain order...
    tests = [
            'runOK',
            'runNOK',
            'clear',
            'syntaxerror',
            'longscript',
            'getvalue_logical',
            'getvalue_complex',
            'getvalue',
            'putvalue',
            'putvalue_logical',
            'getput',
            'getput_complex',
            'getput_logical',
            'getput_string',
            'check_order_mult',
            'check_order_vector',
            ]
    return unittest.TestSuite(map(MatlabTestCase,tests))

