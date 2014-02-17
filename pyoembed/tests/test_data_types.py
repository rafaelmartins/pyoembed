import unittest

from pyoembed.data_types import BaseDataType
from pyoembed.exceptions import DataTypeException


class DataTypesTestCase(unittest.TestCase):

    def test_ok(self):

        class MyDataType(BaseDataType):

            priority = 0
            name = 'lol'
            required_fields = ['bola', 'guda']

        dt = MyDataType()
        data = {'type': 'lol', 'bola': 'arco', 'guda': 'iro', 'version': '1.0'}
        self.assertTrue(dt.type_supported(data))
        dt.validate_data(data)

    def test_fail(self):

        class MyDataType(BaseDataType):

            priority = 0
            name = 'lol'
            required_fields = ['bola', 'guda']

        dt = MyDataType()
        data = {'type': 'hehe', 'bola': 'arco', 'guda': 'iro',
                'version': '1.0'}
        self.assertFalse(dt.type_supported(data))

    def test_no_version(self):

        class MyDataType(BaseDataType):

            priority = 0
            name = 'lol'
            required_fields = ['bola', 'guda']

        dt = MyDataType()
        data = {'type': 'lol', 'bola': 'arco', 'guda': 'iro'}
        self.assertTrue(dt.type_supported(data))
        with self.assertRaises(DataTypeException):
            dt.validate_data(data)

    def test_no_required_field(self):

        class MyDataType(BaseDataType):

            priority = 0
            name = 'lol'
            required_fields = ['bola', 'guda']

        dt = MyDataType()
        data = {'type': 'lol', 'bola': 'arco', 'version': '1.0'}
        self.assertTrue(dt.type_supported(data))
        with self.assertRaises(DataTypeException):
            dt.validate_data(data)
