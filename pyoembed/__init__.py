import requests
from collections import OrderedDict
from urllib import urlencode
from urlparse import parse_qsl, urlsplit, urlunsplit

from pyoembed.data_types import get_data_type
from pyoembed.exceptions import DataTypeException, ParserException, \
    ProviderException, PyOembedException
from pyoembed.parsers import get_parser
from pyoembed.providers import get_provider


def oEmbed(url, maxwidth=None, maxheight=None):
    provider = get_provider(url)
    if provider is None:
        raise ProviderException('No provider found for url: %s' % url)
    oembed_url = provider.oembed_url(url)

    # lets parse url to append our own width/height parameters
    scheme, netloc, path, query_string, fragment = urlsplit(oembed_url)
    query_params = OrderedDict(parse_qsl(query_string))

    # append width/height parameters
    if maxwidth is not None:
        query_params['maxwidth'] = [int(maxwidth)]
    if maxheight is not None:
        query_params['maxheight'] = [int(maxheight)]

    # rebuild url
    final_url = urlunsplit((scheme, netloc, path,
                            urlencode(query_params, True), fragment))

    # do actual oEmbed request
    response = requests.get(final_url)
    if not response.ok:
        raise PyOembedException('Failed to do oEmbed request: %s' % url)

    # get content type
    content_type = response.headers.get('content-type', None)
    parser = get_parser(content_type)
    if parser is None:
        raise ParserException('Failed to find a parser for url: %s' % url)

    # parse oEmbed request
    data = parser.content_parse(response.text)

    # get data type
    data_type = get_data_type(data)
    if data_type is None:
        raise DataTypeException('Failed to find a data type for url: %s' % url)

    # validate data
    data_type.validate_data(data)

    # return data :)
    return data
