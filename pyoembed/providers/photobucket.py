from pyoembed.providers import BaseProvider


class JustinTVProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://i*.photobucket.com/albums/*']
    oembed_endpoint = 'http://photobucket.com/oembed'
