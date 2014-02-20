from pyoembed.providers import BaseProvider


class ChirbitProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://chirb.it/*']
    oembed_endpoint = 'http://chirb.it/oembed.json'
