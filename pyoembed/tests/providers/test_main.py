import re
import unittest

from pyoembed.providers import BaseProvider


class MyProvider(BaseProvider):

    priority = 1
    oembed_endpoint = 'http://google.com/?format={format}'
    oembed_schemas = [re.compile('http://bola\.com/guda/.*'),
                      'http://google.com/*/foo']


class BaseProviderTestCase(unittest.TestCase):

    def test_url_supported(self):
        provider = MyProvider()
        self.assertTrue(provider.url_supported('http://bola.com/guda/arco'))
        self.assertTrue(provider.url_supported('http://google.com/bola/foo'))
        self.assertFalse(provider.url_supported('http://arcoiro.com/bola'))

    def test_oembed_url(self):
        provider = MyProvider()
        self.assertEqual(provider.oembed_url('http://bola.com/guda/arco'),
                         'http://google.com/?format=json&url=http%3A%2F%2F'
                         'bola.com%2Fguda%2Farco')
        self.assertEqual(provider.oembed_url('http://google.com/bola/foo'),
                         'http://google.com/?format=json&url=http%3A%2F%2F'
                         'google.com%2Fbola%2Ffoo')

    def test_build_re(self):
        provider = MyProvider()
        _re = provider._build_re('http://google.com/*/foo')
        self.assertEqual(_re.pattern, '^http\\:\\/\\/google\\.com\\/.*\\/foo$')

    def test_get_re(self):
        provider = MyProvider()
        _re = provider._get_re()
        self.assertEqual(len(_re), 2)
        self.assertEqual(_re[0].pattern, 'http://bola\.com/guda/.*')
        self.assertEqual(_re[1].pattern,
                         '^http\\:\\/\\/google\\.com\\/.*\\/foo$')
        self.assertEqual(len(provider._re_schemas), 2)
        self.assertEqual(provider._re_schemas[0].pattern,
                         'http://bola\.com/guda/.*')
        self.assertEqual(provider._re_schemas[1].pattern,
                         '^http\\:\\/\\/google\\.com\\/.*\\/foo$')
