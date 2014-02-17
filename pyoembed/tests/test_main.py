import mock
import unittest

from pyoembed import oEmbed
from pyoembed.exceptions import DataTypeException, ParserException, \
    ProviderException, PyOembedException


class oEmbedTestCase(unittest.TestCase):

    @mock.patch('pyoembed.get_provider')
    def test_provider_not_found(self, get_provider):
        get_provider.return_value = None
        with self.assertRaises(ProviderException):
            oEmbed('foo')

    @mock.patch('pyoembed.get_provider')
    @mock.patch('pyoembed.requests.get')
    def test_url_parsing(self, get, get_provider):
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.ok = False
        provider.oembed_url.return_value = 'http://google.com/foo'
        with self.assertRaises(PyOembedException):
            oEmbed('foo')
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo')

    @mock.patch('pyoembed.get_provider')
    @mock.patch('pyoembed.requests.get')
    def test_maxwidth(self, get, get_provider):
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.ok = False
        provider.oembed_url.return_value = 'http://google.com/foo'
        with self.assertRaises(PyOembedException):
            oEmbed('foo', maxwidth=100)
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo?maxwidth=100')

    @mock.patch('pyoembed.get_provider')
    @mock.patch('pyoembed.requests.get')
    def test_maxheight(self, get, get_provider):
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.ok = False
        provider.oembed_url.return_value = 'http://google.com/foo'
        with self.assertRaises(PyOembedException):
            oEmbed('foo', maxheight=100)
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo?maxheight=100')

    @mock.patch('pyoembed.get_parser')
    @mock.patch('pyoembed.get_provider')
    @mock.patch('pyoembed.requests.get')
    def test_parser_not_found(self, get, get_provider, get_parser):
        get_parser.return_value = None
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.ok = True
        provider.oembed_url.return_value = 'http://google.com/foo'
        with self.assertRaises(ParserException):
            oEmbed('foo')
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo')

    @mock.patch('pyoembed.get_data_type')
    @mock.patch('pyoembed.get_parser')
    @mock.patch('pyoembed.get_provider')
    @mock.patch('pyoembed.requests.get')
    def test_data_type_not_found(self, get, get_provider, get_parser,
                                 get_data_type):
        get_data_type.return_value = None
        get_parser.return_value = parser = mock.Mock()
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.ok = True
        response.text = 'bola'
        parser.content_parse.return_value = {}
        provider.oembed_url.return_value = 'http://google.com/foo'
        with self.assertRaises(DataTypeException):
            oEmbed('foo')
        parser.content_parse.assert_called_once_with('bola')
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo')

    @mock.patch('pyoembed.get_data_type')
    @mock.patch('pyoembed.get_parser')
    @mock.patch('pyoembed.get_provider')
    @mock.patch('pyoembed.requests.get')
    def test_success(self, get, get_provider, get_parser, get_data_type):
        get_data_type.return_value = data_type = mock.Mock()
        get_parser.return_value = parser = mock.Mock()
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.ok = True
        response.text = 'bola'
        parser.content_parse.return_value = {}
        provider.oembed_url.return_value = 'http://google.com/foo'
        oEmbed('foo')
        data_type.validate_data.assert_called_once_with({})
        parser.content_parse.assert_called_once_with('bola')
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo')
