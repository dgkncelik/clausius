from .base_validator import BaseValidator
from .exception import ValidatorError


class BoolValidator(BaseValidator):
    def __init__(self, **kwargs):
        super(BoolValidator, self).__init__(**kwargs)

    def validate(self, value, **kwargs):
        if not isinstance(value, bool):
            raise ValidatorError('Value is not instance of bool')

        return super(BoolValidator, self).validate(**kwargs)
