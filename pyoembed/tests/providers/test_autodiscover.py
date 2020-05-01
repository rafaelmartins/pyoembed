from unittest import mock
import unittest
import pytest

from pyoembed.exceptions import ProviderException
from pyoembed.providers.autodiscover import AutoDiscoverProvider
from pyoembed.tests import get_fixture


class AutoDiscoverProviderTestCase(unittest.TestCase):

    def setUp(self):
        self.provider = AutoDiscoverProvider()
        self.url = 'http://google.com'

    def test_url_supported(self):
        self.assertTrue(self.provider.url_supported(self.url))

    @pytest.mark.asyncio
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_oembed_url_request_failed(self, get):
        get.return_value = response = mock.Mock()
        response.status = 500
        response.text = mock.AsyncMock(
            return_value=get_fixture('autodiscover-both.html'))
        with self.assertRaises(ProviderException):
            await self.provider.oembed_url(self.url)

    @pytest.mark.asyncio
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_oembed_url_none(self, get):
        get.return_value = response = mock.Mock()
        response.status = 200
        response.text = mock.AsyncMock(
            return_value=get_fixture('autodiscover-none.html'))
        with self.assertRaises(ProviderException):
            await self.provider.oembed_url(self.url)

    @pytest.mark.asyncio
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_oembed_url_both(self, get):
        get.return_value = response = mock.Mock()
        response.status = 200
        response.text = mock.AsyncMock(
            return_value=get_fixture('autodiscover-both.html'))
        self.assertEqual(await self.provider.oembed_url(self.url),
                         'http://www.youtube.com/oembed?url=http%3A%2F%2F'
                         'www.youtube.com%2Fwatch%3Fv%3D2nLsvPBqeZ8'
                         '&format=json')

    @pytest.mark.asyncio
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_oembed_url_json(self, get):
        get.return_value = response = mock.Mock()
        response.status = 200
        response.text = mock.AsyncMock(
            return_value=get_fixture('autodiscover-json.html'))
        self.assertEqual(await self.provider.oembed_url(self.url),
                         'http://www.youtube.com/oembed?url=http%3A%2F%2F'
                         'www.youtube.com%2Fwatch%3Fv%3D2nLsvPBqeZ8'
                         '&format=json')

    @pytest.mark.asyncio
    @mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock)
    async def test_oembed_url_xml(self, get):
        get.return_value = response = mock.Mock()
        response.status = 200
        response.text = mock.AsyncMock(
            return_value=get_fixture('autodiscover-xml.html'))
        self.assertEqual(await self.provider.oembed_url(self.url),
                         'http://www.youtube.com/oembed?url=http%3A%2F%2F'
                         'www.youtube.com%2Fwatch%3Fv%3D2nLsvPBqeZ8'
                         '&format=xml')
