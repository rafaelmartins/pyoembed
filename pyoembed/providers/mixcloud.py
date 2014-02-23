from pyoembed.providers import BaseProvider


class MixcloudProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://www.mixcloud.com/*/*/']
    oembed_endpoint = 'http://www.mixcloud.com/oembed/'
