from pyoembed.providers import BaseProvider


class ImgurProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://i.imgur.com/*',
                      'http://imgur.com/*']
    oembed_endpoint = 'http://api.imgur.com/oembed'
