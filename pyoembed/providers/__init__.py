import re
import sys
from abc import ABCMeta, abstractproperty
from collections import OrderedDict

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

try:
    from urlparse import parse_qsl, urlsplit, urlunsplit
except ImportError:
    from urllib.parse import parse_qsl, urlsplit, urlunsplit

from pyoembed.utils import get_metaclass_objects

str_type = str
if sys.version_info[0] == 2:
    str_type = basestring


class BaseProvider(object):
    __metaclass__ = ABCMeta

    _re_schemas = None

    @abstractproperty
    def priority(self):
        pass  # pragma: no cover

    @abstractproperty
    def oembed_endpoint(self):
        pass  # pragma: no cover

    @abstractproperty
    def oembed_schemas(self):
        pass  # pragma: no cover

    def _build_re(self, schema):
        pieces = schema.split('*')
        pieces = map(re.escape, pieces)
        return re.compile(r'^%s$' % r'.*'.join(pieces))

    def _get_re(self):
        if self._re_schemas is not None:
            return self._re_schemas
        _re_schemas = []
        for schema in self.oembed_schemas:
            if not isinstance(schema, str_type):
                _re_schemas.append(schema)
            else:
                _re_schemas.append(self._build_re(schema))
        self._re_schemas = _re_schemas
        return self._re_schemas

    def url_supported(self, url):
        for regex in self._get_re():
            if regex.match(url):
                return True
        return False

    def oembed_url(self, url):
        oembed_endpoint = self.oembed_endpoint.replace('{format}', 'json')
        scheme, netloc, path, qs, fragment = urlsplit(oembed_endpoint)
        query_params = OrderedDict(parse_qsl(qs))
        query_params['url'] = url
        return urlunsplit((scheme, netloc, path,
                           urlencode(query_params, True), fragment))


def get_provider(url):
    providers = get_metaclass_objects(__name__, BaseProvider,
                                      lambda x: x.priority)
    for provider in providers:
        if provider.url_supported(url):
            return provider
