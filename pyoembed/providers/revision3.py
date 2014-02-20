from pyoembed.providers import BaseProvider


class Revision3Provider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://www.revision3.com/*',
                      'http://revision3.com/*']
    oembed_endpoint = 'http://revision3.com/api/oembed/'
