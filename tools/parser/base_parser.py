"""
Base parser class
Parsers aim to parse data from one to other format with parse(value) method

ex:

BaseParser(arg1=value, ...).parser(value)
"""


class BaseParser(object):
    def __init__(self, **kwargs):
        self._initial_parameters = kwargs

    def parse(self, value, **kwargs):
        """
        :param value: data which will parse
        :param kwargs: return parsed value
        :raisae: ParserError exception on non parsed data
        """
        return value
