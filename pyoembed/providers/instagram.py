from pyoembed.providers import BaseProvider


class InstagramProvider(BaseProvider):

    priority = 10
    oembed_schemas = ['https://instagram.com/p/*',
                      'https://instagr.am/p/*',
                      'https://www.instagram.com/p/*',
                      'https://www.instagr.am/p/*'
                      'http://instagram.com/p/*',
                      'http://instagr.am/p/*',
                      'http://www.instagram.com/p/*',
                      'http://www.instagr.am/p/*']

    oembed_endpoint = 'https://api.instagram.com/oembed'
