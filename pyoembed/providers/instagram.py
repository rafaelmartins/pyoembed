from pyoembed.providers import BaseProvider


class InstagramProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://instagram.com/p/*',
                      'http://instagr.am/p/*']
    oembed_endpoint = 'http://api.instagram.com/oembed'
