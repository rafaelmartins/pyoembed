from abc import ABCMeta, abstractmethod, abstractproperty

from pyoembed.utils import get_metaclass_objects


class BaseParser(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def priority(self):
        pass

    @abstractmethod
    def content_supported(self, content_type):
        pass

    @abstractmethod
    def content_parse(self, content):
        pass


def get_parser(content_type):
    parsers = get_metaclass_objects(__name__, BaseParser, lambda x: x.priority)
    for parser in parsers:
        if parser.content_supported(content_type):
            return parser
