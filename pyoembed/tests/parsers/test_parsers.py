import unittest

from pyoembed.parsers.json_parser import JsonParser
from pyoembed.parsers.xml_parser import XmlParser
from pyoembed.tests import get_fixture


class ParsersTestCase(unittest.TestCase):

    def test_parsers_returns_same_stuff(self):
        xml_parser = XmlParser()
        json_parser = JsonParser()
        xml = xml_parser.content_parse(get_fixture('sample-video.xml'))
        json = json_parser.content_parse(get_fixture('sample-video.json'))
        self.assertEqual(xml, json)
