from abc import ABCMeta, abstractproperty

from pyoembed.exceptions import DataTypeException
from pyoembed.utils import get_metaclass_objects


class BaseDataType(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def priority(self):
        pass

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def required_fields(self):
        pass

    def type_supported(self, data):
        if 'type' in data:
            if data['type'] == self.name:
                return True
        return False

    def validate_data(self, data):
        required = self.required_fields + ['version']
        not_found = []
        for field in required:
            if field not in data.keys():
                not_found.append(field)
        if len(not_found) > 0:
            raise DataTypeException('Required fields not found: %r' %
                                    not_found)


def get_data_type(data):
    data_types = get_metaclass_objects(__name__, BaseDataType,
                                       lambda x: x.priority)
    for data_type in data_types:
        if data_type.type_supported(data):
            return data_type
