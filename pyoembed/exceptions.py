class PyOembedException(Exception):
    pass


class ParserException(PyOembedException):
    pass


class ProviderException(PyOembedException):
    pass


class DataTypeException(PyOembedException):
    pass
