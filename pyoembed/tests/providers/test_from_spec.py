import mock
import unittest

from pyoembed.exceptions import ProviderException
from pyoembed.providers.from_spec import FromSpecProvider
from pyoembed.tests import get_fixture


class AutoDiscoverProviderTestCase(unittest.TestCase):

    def setUp(self):
        self.provider = FromSpecProvider()
        self.url = 'https://www.youtube.com/watch?v=2nLsvPBqeZ8'

    def test_url_supported(self):
        self.assertTrue(self.provider.url_supported(self.url))

    @mock.patch('pyoembed.providers.from_spec.requests.get')
    def test_oembed_url_json(self, get):
        get.return_value = response = mock.Mock()
        response.ok = True
        response.json = get_fixture('youtube.json')
        self.assertEqual(self.provider.oembed_url(self.url),
                         'https://www.youtube.com/oembed?url=https%3A%2F%2F'
                         'www.youtube.com%2Fwatch%3Fv%3D2nLsvPBqeZ8')
