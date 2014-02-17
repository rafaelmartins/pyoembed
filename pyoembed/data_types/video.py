from pyoembed.data_types import BaseDataType


class VideoDataType(BaseDataType):

    priority = 1
    name = 'video'
    required_fields = ['html', 'width', 'height']
