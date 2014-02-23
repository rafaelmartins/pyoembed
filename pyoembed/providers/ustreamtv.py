from pyoembed.providers import BaseProvider


class UstreamTVProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://ustream.tv/*',
                      'http://www.ustream.tv/*',
                      'http://ustream.com/*',
                      'http://www.ustream.com/*']
    oembed_endpoint = 'http://www.ustream.tv/oembed'
