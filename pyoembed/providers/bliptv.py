from pyoembed.providers import BaseProvider


class BlipTVProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://blip.tv/*/*',
                      'http://www.blip.tv/*/*']
    oembed_endpoint = 'http://blip.tv/oembed/'
