from pyoembed.providers import BaseProvider


class SpotifyProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://open.spotify.com/*',
                      'http://play.spotify.com/*',
                      'https://open.spotify.com/*',
                      'https://play.spotify.com/*']
    oembed_endpoint = 'https://embed.spotify.com/oembed/'
