from pyoembed.providers import BaseProvider


class DotsubProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://dotsub.com/view/*',
                      'https://dotsub.com/view/*']
    oembed_endpoint = 'http://dotsub.com/services/oembed'
