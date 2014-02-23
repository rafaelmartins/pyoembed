from pyoembed.providers import BaseProvider


class JustinTVProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://www.justin.tv/*']
    oembed_endpoint = 'http://api.justin.tv/api/embed/from_url.{format}'
