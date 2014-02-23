from pyoembed.providers import BaseProvider


class GeoHlippDeProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://geo-en.hlipp.de/*',
                      'http://geo.hlipp.de/*',
                      'http://germany.geograph.org/*']
    oembed_endpoint = 'http://geo.hlipp.de/restapi.php/api/oembed'
