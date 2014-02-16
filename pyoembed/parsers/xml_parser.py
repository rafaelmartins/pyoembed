from xml.etree import cElementTree as etree

from pyoembed.parsers import BaseParser


class XmlParser(BaseParser):

    priority = 2

    def content_supported(self, content_type):
        ct = content_type.lower()
        return 'application/xml' in ct or 'text/xml' in ct

    def content_parse(self, content):
        element = etree.XML(content)
        rv = {}
        for i in element.getiterator():
            if i.tag in ['oembed']:
                continue
            tag = i.tag
            text = i.text
            if 'height' in tag or 'width' in tag:
                text = int(text)
            rv[tag] = text
        return rv
