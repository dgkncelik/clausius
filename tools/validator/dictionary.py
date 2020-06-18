from .base_validator import BaseValidator
from .exception import ValidatorError


class DictionaryValidator(BaseValidator):
    def __init__(self, **kwargs):
        super(DictionaryValidator, self).__init__(**kwargs)

    def validate(self, value, min_length=None, max_length=None, **kwargs):
        if not isinstance(value, list):
            raise ValidatorError('Value is not instance of list')

        if isinstance(min_length, int) and len(value) < min_length:
            raise ValidatorError('Value length is lower then min_value')

        if isinstance(max_length, int) and len(value) > max_length:
            raise ValidatorError('Value length is higher then max_value')

        return super(DictionaryValidator, self).validate(**kwargs)
