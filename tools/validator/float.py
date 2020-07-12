from .base_validator import BaseValidator
from .exception import ValidatorError

"""
Float validator class
"""


class FloatValidator(BaseValidator):
    def __init__(self, **kwargs):
        """
        :param kwargs:
        :param min_value: minimum value of float to validate
        :param max_value: maximum value of float to validate
        """
        self.min_value = kwargs.get('min_value', None)
        self.max_value = kwargs.get('max_value', None)
        super(FloatValidator, self).__init__(**kwargs)

    def validate(self, value, **kwargs):
        if not isinstance(value, float):
            raise ValidatorError('Value is [%s] not instance of int' % value)

        if isinstance(self.min_value, float) and value < self.min_value:
            raise ValidatorError('Value is [%s] lower then min_value [%s]' % (value, self.min_value))

        if isinstance(self.max_value, float) and value > self.max_value:
            raise ValidatorError('Value is [%s] higher then max_value [%s]' % (value, self.max_value))

        return super(FloatValidator, self).validate(value, **kwargs)
