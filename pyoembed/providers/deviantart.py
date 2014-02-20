from pyoembed.providers import BaseProvider


class DeviantartProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['http://*.deviantart.com/art/*',
                      'http://*.deviantart.com/*#/d*',
                      'http://fav.me/*', 'http://sta.sh/*']
    oembed_endpoint = 'http://backend.deviantart.com/oembed'
