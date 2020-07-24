from model.field.exception import FieldException
from tools.validator.base_validator import BaseValidator
"""
Base Field class
Fields are holding data in key-value pair
Fields can have validators and parsers to parse or validate the value

Key and value can be assigned on init or later
Has validate and parse methods

ex:
BaseField(key='x', value='y', validators=[DictionaryValidator, ...], parsers=[BaseParser, ...] )
BaseField().validate()
BaseField().parse()
"""


class BaseField(object):
    def __init__(self, **kwargs):
        self._initial_parameters = kwargs
        self._key = kwargs.get('key', None)
        self._value = kwargs.get('value', None)
        self._validators = kwargs.get('validators', [])
        self._parsers = kwargs.get('parsers', [])

    def validate(self):
        pass

    def parse(self):
        pass

    @property
    def validators(self):
        return self._validators

    @validators.setter
    def validators(self, v):
        self._validate_validators(v)
        self._validators = v

    def parsers(self):
        pass

    def key(self):
        pass

    def value(self):
        pass

    @staticmethod
    def _validate_validators(v_list):
        if not(v_list, list):
            raise FieldException('Validators must be list instance')

        for v in v_list:
            if not isinstance(v, BaseValidator) or not issubclass(v.__class__, BaseValidator):
                raise FieldException('Validators must be BaseValidator instance/subclass')
