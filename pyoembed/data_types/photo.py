from pyoembed.data_types import BaseDataType


class PhotoDataType(BaseDataType):

    priority = 2
    name = 'photo'
    required_fields = ['url', 'width', 'height']
