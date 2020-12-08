import cgi

import requests
from bs4 import BeautifulSoup

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from pyoembed.exceptions import ProviderException
from pyoembed.providers import BaseProvider


class AutoDiscoverProvider(BaseProvider):

    priority = 99999999  # should be the last, always.

    # following properties are not used because we are overriding all the
    # methods that used them.
    oembed_endpoint = None
    oembed_schemas = None

    def url_supported(self, url):
        return True  # autodiscover supports anything :)

    def oembed_url(self, url):
        response = requests.get(url)

        if not response.ok:
            raise ProviderException('Failed to auto-discover oEmbed provider '
                                    'for url: %s' % url)

        content_type = response.headers.get('Content-Type')
        if content_type is None:
            charset = None
        else:
            mime_type, parameters = cgi.parse_header(content_type)
            charset = parameters.get('charset')
        bs = BeautifulSoup(response.content, 'lxml', from_encoding=charset)

        # we prefer json over xml, so let's try it first :)
        oembed_url = bs.find('link', type='application/json+oembed', href=True)

        # if json isn't available, try xml
        if oembed_url is None:
            oembed_url = bs.find('link', type='text/xml+oembed', href=True)

        if oembed_url is None:
            raise ProviderException('No oEmbed url found: %s' % url)

        return urljoin(url, oembed_url['href'])
