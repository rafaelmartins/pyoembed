from urllib import urlencode
from urlparse import parse_qs, urlsplit, urlunsplit

from pyoembed.exceptions import ProviderException
from pyoembed.providers import get_provider


def oEmbed(url, maxwidth=None, maxheight=None):
    provider = get_provider(url)
    if provider is None:
        raise ProviderException('No provider found for url: %s' % url)
    oembed_url = provider.oembed_url(url)

    # lets parse url to append our own width/height parameters
    scheme, netloc, path, query_string, fragment = urlsplit(oembed_url)
    query_params = parse_qs(query_string)

    if maxwidth is not None:
        query_params['maxwidth'] = [int(maxwidth)]
    if maxheight is not None:
        query_params['maxheight'] = [int(maxheight)]

    final_url = urlunsplit((scheme, netloc, path,
                            urlencode(query_params, True), fragment))

    print final_url
