from .base_validator import BaseValidator
from .exception import ValidatorError

class IntegerValidator(BaseValidator):
    @staticmethod
    def validate(value, min_value=None, max_value=None, **kwargs):
        if not isinstance(value, int):
            raise ValidatorError('Value is not instance of int')

        if isinstance(min_value, int) and value < min_value:
            raise ValidatorError('Value is lower then min_value')

        if isinstance(max_value, int) and value > max_value:
            raise ValidatorError('Value is higher then max_value')

        return super.validate(value, kwargs)