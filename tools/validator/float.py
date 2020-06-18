from .base_validator import BaseValidator
from .exception import ValidatorError


class FloatValidator(BaseValidator):
    def __init__(self, **kwargs):
        super(FloatValidator, self).__init__(**kwargs)

    def validate(self, value, min_value=None, max_value=None, **kwargs):
        if not isinstance(value, float):
            raise ValidatorError('Value is not instance of int')

        if isinstance(min_value, float) and value < min_value:
            raise ValidatorError('Value is lower then min_value')

        if isinstance(max_value, float) and value > max_value:
            raise ValidatorError('Value is higher then max_value')

        return super(FloatValidator, self).validate(**kwargs)
