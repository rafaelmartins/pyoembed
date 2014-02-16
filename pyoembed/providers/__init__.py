import os
from abc import ABCMeta, abstractmethod, abstractproperty


class ProviderException(Exception):
    pass


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


def _get_providers():
    cwd = os.path.dirname(os.path.abspath(__file__))
    imported = []
    for provider_file in os.listdir(cwd):
        provider, ext = os.path.splitext(provider_file)
        if ext not in ['.py', '.pyc', '.pyo']:
            continue
        if provider in ['__init__']:
            continue
        if provider not in imported:
            __import__('pyoembed.providers.%s' % provider)
            imported.append(provider)
    providers = [provider() for provider in BaseProvider.__subclasses__()]
    return sorted(providers, key=lambda x: x.priority)


providers = _get_providers()
del _get_providers


def get_provider(url):
    for provider in providers:
        if provider.url_supported(url):
            return provider