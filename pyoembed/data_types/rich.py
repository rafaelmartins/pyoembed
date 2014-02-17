from pyoembed.data_types import BaseDataType


class RichDataType(BaseDataType):

    priority = 3
    name = 'rich'
    required_fields = ['html', 'width', 'height']
