import json

from pyoembed.parsers import BaseParser


class JsonParser(BaseParser):

    priority = 1

    def content_supported(self, content_type):
        ct = content_type.lower()
        return 'application/json' in ct or 'text/json' in ct or \
               'application/javascript' in ct or 'text/javascript' in ct

    def content_parse(self, content):
        return json.loads(content)
