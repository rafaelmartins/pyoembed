import unittest
from unittest import mock
import pytest

from pyoembed import oEmbed
from pyoembed.exceptions import DataTypeException, ParserException, \
    ProviderException, PyOembedException


class oEmbedTestCase(unittest.TestCase):

    @pytest.mark.asyncio
    @mock.patch('pyoembed.get_provider')
    async def test_provider_not_found(self, get_provider):
        get_provider.return_value = None
        with self.assertRaises(ProviderException):
            await oEmbed('foo')

    @pytest.mark.asyncio
    @mock.patch('pyoembed.get_provider')
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_url_parsing(self, get, get_provider):
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.status = 500
        provider.oembed_url = mock.AsyncMock(return_value='http://google.com/foo')
        with self.assertRaises(PyOembedException):
            await oEmbed('foo')
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo')

    @pytest.mark.asyncio
    @mock.patch('pyoembed.get_provider')
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_maxwidth(self, get, get_provider):
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.status = 500
        provider.oembed_url = mock.AsyncMock(return_value='http://google.com/foo')
        with self.assertRaises(PyOembedException):
            await oEmbed('foo', maxwidth=100)
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo?maxwidth=100')

    @pytest.mark.asyncio
    @mock.patch('pyoembed.get_provider')
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_maxheight(self, get, get_provider):
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.status = 500
        provider.oembed_url = mock.AsyncMock(return_value='http://google.com/foo')
        with self.assertRaises(PyOembedException):
            await oEmbed('foo', maxheight=100)
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo?maxheight=100')

    @pytest.mark.asyncio
    @mock.patch('pyoembed.get_parser')
    @mock.patch('pyoembed.get_provider')
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_parser_not_found(self, get, get_provider, get_parser):
        get_parser.return_value = None
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.status = 200
        provider.oembed_url = mock.AsyncMock(return_value='http://google.com/foo')
        with self.assertRaises(ParserException):
            await oEmbed('foo')
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo')

    @pytest.mark.asyncio
    @mock.patch('pyoembed.get_data_type')
    @mock.patch('pyoembed.get_parser')
    @mock.patch('pyoembed.get_provider')
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_data_type_not_found(self, get, get_provider, get_parser,
                                 get_data_type):
        get_data_type.return_value = None
        get_parser.return_value = parser = mock.Mock()
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.status = 200
        response.text = mock.AsyncMock(return_value='bola')
        parser.content_parse.return_value = {}
        provider.oembed_url = mock.AsyncMock(return_value='http://google.com/foo')
        with self.assertRaises(DataTypeException):
            await oEmbed('foo')
        parser.content_parse.assert_called_once_with('bola')
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo')

    @pytest.mark.asyncio
    @mock.patch('pyoembed.get_data_type')
    @mock.patch('pyoembed.get_parser')
    @mock.patch('pyoembed.get_provider')
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_success(self, get, get_provider, get_parser, get_data_type):
        get_data_type.return_value = data_type = mock.Mock()
        get_parser.return_value = parser = mock.Mock()
        get_provider.return_value = provider = mock.Mock()
        get.return_value = response = mock.Mock()
        response.status = 200
        response.text = mock.AsyncMock(return_value='bola')
        parser.content_parse.return_value = {}
        provider.oembed_url = mock.AsyncMock(return_value='http://google.com/foo')
        await oEmbed('foo')
        data_type.validate_data.assert_called_once_with({})
        parser.content_parse.assert_called_once_with('bola')
        provider.oembed_url.assert_called_once_with('foo')
        get.assert_called_once_with('http://google.com/foo')
