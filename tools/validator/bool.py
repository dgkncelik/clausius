from .base_validator import BaseValidator
from .exception import ValidatorError

"""
Bool validator class
"""


class BoolValidator(BaseValidator):
    def __init__(self, **kwargs):
        super(BoolValidator, self).__init__(**kwargs)

    def validate(self, value, **kwargs):
        if not isinstance(value, bool):
            raise ValidatorError('Value [%s] is not instance of bool' % value)

        return super(BoolValidator, self).validate(value, **kwargs)
