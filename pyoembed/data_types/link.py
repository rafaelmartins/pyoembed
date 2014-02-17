from pyoembed.data_types import BaseDataType


class LinkDataType(BaseDataType):

    priority = 4
    name = 'link'
    required_fields = []
