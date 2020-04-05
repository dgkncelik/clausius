from .base_validator import BaseValidator
from .exception import ValidatorError

class StringValidator(BaseValidator):
    @staticmethod
    def validate(value, allow_whitespace=True, max_length=None, min_length=None, **kwargs):
        if not isinstance(value, str):
            raise ValidatorError('Value is not instance of str')
        
        if isinstance(min_length, int) and len(value) < min_length:
            raise ValidatorError('Value length lower then minimum')
        
        if isinstance(max_length, int) and len(value) > max_length:
            raise ValidatorError('Value length higher then maximum') 

        if not allow_whitespace and len(value.strip()) == 0:
            raise ValidatorError('Value is composed only with whitespace')

        return super.validate(value, **kwargs)