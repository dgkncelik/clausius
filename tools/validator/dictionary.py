from .base_validator import BaseValidator
from .exception import ValidatorError

"""
Dictionary validator class
"""


class DictionaryValidator(BaseValidator):
    def __init__(self, **kwargs):
        """
        :param kwargs:
        :param min_length: minimum key size of the dictionary
        :param max_length: maximum key size of the dictionary
        """
        self.min_length = kwargs.get('min_length', None)
        self.max_length = kwargs.get('max_length', None)
        super(DictionaryValidator, self).__init__(**kwargs)

    def validate(self, value, **kwargs):
        if not isinstance(value, list):
            raise ValidatorError('Value is not instance of list')

        if isinstance(self.min_length, int) and len(value) < self.min_length:
            raise ValidatorError('Value length is [%s] lower then min_length [%s]' % (len(value), self.min_length))

        if isinstance(self.max_length, int) and len(value) > self.max_length:
            raise ValidatorError('Value length is [%s] higher then max_length [%s]' % (len(value), self.max_length))

        return super(DictionaryValidator, self).validate(value, **kwargs)
