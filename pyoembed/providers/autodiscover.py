import requests
from bs4 import BeautifulSoup
from urlparse import urljoin

from pyoembed.exceptions import ProviderException
from pyoembed.providers import BaseProvider


class AutoDiscoverProvider(BaseProvider):

    priority = 9999  # should be the last, always.

    def url_supported(self, url):
        return True  # autodiscover supports anything :)

    def oembed_url(self, url):
        response = requests.get(url)

        if not response.ok:
            raise ProviderException('Failed to auto-discover oEmbed provider '
                                    'for url: %s' % url)

        bs = BeautifulSoup(response.text)

        # we prefer json over xml, so let's try it first :)
        oembed_url = bs.find('link', type='application/json+oembed', href=True)

        # if json isn't available, try xml
        if oembed_url is None:
            oembed_url = bs.find('link', type='text/xml+oembed', href=True)

        if oembed_url is None:
            raise ProviderException('No oEmbed url found: %s' % url)

        return urljoin(url, oembed_url['href'])
