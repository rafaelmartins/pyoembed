from pyoembed.providers import BaseProvider


class SapoPTProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://videos.sapo.pt/*']
    oembed_endpoint = 'http://videos.sapo.pt/oembed'
