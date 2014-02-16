from abc import ABCMeta, abstractmethod, abstractproperty

from pyoembed.utils import get_metaclass_objects


class BaseProvider(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def priority(self):
        pass

    @abstractmethod
    def url_supported(self, url):
        pass

    @abstractmethod
    def oembed_url(self, url):
        pass


def get_provider(url):
    providers = get_metaclass_objects(__name__, BaseProvider,
                                      lambda x: x.priority)
    for provider in providers:
        if provider.url_supported(url):
            return provider
