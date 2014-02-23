from pyoembed.providers import BaseProvider


class GeographOrgUkProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://*.geograph.org.uk/*',
                      'http://*.geograph.co.uk/*',
                      'http://*.geograph.ie/*',

                      # not tested
                      'http://*.wikimedia.org/*_geograph.org.uk_*']
    oembed_endpoint = 'http://api.geograph.org.uk/api/oembed'
