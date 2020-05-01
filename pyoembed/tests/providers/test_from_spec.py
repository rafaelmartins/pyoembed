from unittest import mock
import unittest
import asyncio

import pytest

from pyoembed.providers.from_spec import FromSpecProvider, load_data
from pyoembed.tests import get_fixture

class AutoDiscoverProviderTestCase(unittest.TestCase):

    def setUp(self):
        self.provider = FromSpecProvider()
        self.url = 'https://www.youtube.com/watch?v=2nLsvPBqeZ8'
        loop = asyncio.new_event_loop()
        loop.run_until_complete(asyncio.Task(load_data(False, loop), loop=loop))

    def test_url_supported(self):
        self.assertTrue(self.provider.url_supported(self.url))

    @pytest.mark.asyncio
    async def test_oembed_url_json(self):
        with mock.patch('aiohttp.ClientSession.get', new_callable=mock.AsyncMock) as get:
            get.return_value = response = mock.Mock()
            response.status = 200
            response.text = mock.AsyncMock(get_fixture('youtube.json'))
            self.assertEqual(await self.provider.oembed_url(self.url),
                             'https://www.youtube.com/oembed?url=https%3A%2F%2F'
                             'www.youtube.com%2Fwatch%3Fv%3D2nLsvPBqeZ8')
