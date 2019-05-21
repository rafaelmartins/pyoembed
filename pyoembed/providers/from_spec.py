import re
from collections import OrderedDict
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
try:
    from urlparse import parse_qsl, urlsplit, urlunsplit
except ImportError:
    from urllib.parse import parse_qsl, urlsplit, urlunsplit

import requests

from pyoembed.providers import BaseProvider


def transform_pattern(pattern):
    if pattern[-1] == '*':
        pattern = pattern[:-1] + r'.+'
    return r'[^/]+'.join(pattern.split('*'))


TESTS = {}
INFO = {}


def load_data(reload=False):
    global TESTS, INFO
    if TESTS and not reload:
        return
    r = requests.get('http://oembed.com/providers.json')
    assert r.ok
    for provider_info in r.json():
        name = provider_info['provider_name']
        INFO[name] = provider_info
        for endpoint in provider_info['endpoints']:
            for scheme in endpoint.get('schemes', []):
                TESTS[re.compile(transform_pattern(scheme))] = name


class FromSpecProvider(BaseProvider):

    priority = 1000  # Not quite the last

    # following properties are not used because we are overriding all the
    # methods that used them.
    oembed_endpoint = None
    oembed_schemas = None

    def __init__(self):
        load_data()

    def url_supported(self, url):
        global TESTS
        for test in TESTS.keys():
            if test.match(url):
                return True
        return False

    def oembed_url(self, url):
        global TESTS, INFO
        for test, name in TESTS.items():
            if test.match(url):
                info = INFO[name]
                endpoints = info['endpoints']
                if len(endpoints) > 1:
                    endpoints = [
                        e for e in endpoints if test.pattern in [
                            transform_pattern(s) for s in e.get('schemes', [])]]
                if len(endpoints):
                    oembed_endpoint = endpoints[0]['url']
                    oembed_endpoint = oembed_endpoint.replace('{format}', 'json')
                    scheme, netloc, path, qs, fragment = urlsplit(oembed_endpoint)
                    query_params = OrderedDict(parse_qsl(qs))
                    query_params['url'] = url
                    return urlunsplit((scheme, netloc, path,
                                       urlencode(query_params, True), fragment))
