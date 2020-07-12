from .base_validator import BaseValidator
from .exception import ValidatorError

"""
String validator class
"""


class StringValidator(BaseValidator):
    def __init__(self, **kwargs):
        """
        :param kwargs:
        :param whitespace: if False emtpy string values will not be validated and raise exception.
        default true
        :param *_length: defines max or min length of string
        """
        self.whitespace = kwargs.get('whitespace', True)
        self.max_length = kwargs.get('max_length', None)
        self.min_length = kwargs.get('min_length', None)
        super(StringValidator, self).__init__(**kwargs)

    def validate(self, value, **kwargs):
        if not isinstance(value, str):
            raise ValidatorError('Value [%s] is not instance of str' % value)
        
        if isinstance(self.min_length, int) and len(value) < self.min_length:
            raise ValidatorError('Value length [%s] lower then minimum' % len(value))
        
        if isinstance(self.max_length, int) and len(value) > self.max_length:
            raise ValidatorError('Value length [%s] higher then maximum' % len(value))

        if not self.whitespace and len(value.strip()) == 0:
            raise ValidatorError('Value is composed only with whitespace')

        return super(StringValidator, self).validate(value, **kwargs)
