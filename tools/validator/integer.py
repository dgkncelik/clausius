from .base_validator import BaseValidator
from .exception import ValidatorError

"""
Integer validator class
"""


class IntegerValidator(BaseValidator):
    def __init__(self, **kwargs):
        """
        :param kwargs:
        :param min_value: mininum value of integer number which will validate
        :param max_value: maximum value of integer number which will validate
        """
        self.min_value = kwargs.get('min_value', None)
        self.max_value = kwargs.get('max_value', None)
        super(IntegerValidator, self).__init__(**kwargs)

    def validate(self, value, **kwargs):
        if not isinstance(value, int):
            raise ValidatorError('Value is not instance of int')

        if isinstance(self.min_value, int) and value < self.min_value:
            raise ValidatorError('Value is [%s] lower then min_value [%s]' % (value, self.min_value))

        if isinstance(self.max_value, int) and value > self.max_value:
            raise ValidatorError('Value is [%s] higher then max_value [%s]' % (value, self.max_value))

        return super(IntegerValidator, self).validate(value, **kwargs)
