from pyoembed.providers import BaseProvider


class RdioProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://www.rdio.com/artist/*/album/*',
                      'http://www.rdio.com/people/*/playlists/*',
                      'http://rd.io/x/*']
    oembed_endpoint = 'http://www.rdio.com/api/oembed/'
