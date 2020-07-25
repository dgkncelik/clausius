from model.field.exception import FieldException, FieldValidationException, FieldParsingException
from tools.validator.base_validator import BaseValidator
from tools.validator.exception import ValidatorError
from tools.parser.base_parser import BaseParser
from tools.parser.exception import ParserError

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
        self._validate_validators(self._validators)

        self._parsers = kwargs.get('parsers', [])
        self._validate_parsers(self._parsers)

    def validate(self):
        """
        Validate value with all validators
        :raises: FieldValidationException if any validator failed to validate
        :return:
        """
        for _validator in self._validators:
            try:
                _validator.validate()
            except ValidatorError as ve:
                raise FieldValidationException(ve)

    def parse(self, pipeline=False):
        """
        :param pipeline: if True data will parse in pipeline manner
        :return: list of parsed results of value
        :raises: FieldParsingException on parsing error
        """
        _result = []
        _temp = self._value
        for p in self._parsers:
            try:
                if pipeline:
                    _temp = p.parse(_temp)
                    _result.append(_temp)
                else:
                    _result.append(p.parse(self._value))
            except ParserError as pe:
                raise FieldParsingException(pe)

        return _result

    @property
    def validators(self):
        """
        get validators
        :return:
        """
        return self._validators

    @validators.setter
    def validators(self, v):
        """
        :param v: list of BaseValidator instance
        :return:
        """
        self._validate_validators(v)
        self._validators = v

    @property
    def parsers(self):
        """
        get parsers
        :return:
        """
        return self._parsers

    @parsers.setter
    def parsers(self, p):
        """
        :param p: list of BaseParser instance
        :return:
        """
        self._validate_parsers(p)
        self._parsers = p

    @property
    def key(self):
        """
        get key
        :return:
        """
        return self._key

    @key.setter
    def key(self, k):
        """
        set key
        :param k: key
        :return:
        """
        self._key = k

    @property
    def value(self):
        """
        get value
        :return:
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        set value
        :param value: value
        :return:
        """
        self._value = value

    @staticmethod
    def _validate_validators(v_list):
        """
        :param v_list: list of validators to be valid instance
        :return:
        """
        if not(v_list, list):
            raise FieldException('Validators must be list instance')

        for v in v_list:
            if not isinstance(v, BaseValidator) or not issubclass(v.__class__, BaseValidator):
                raise FieldException('Validators must be BaseValidator instance/subclass')

    @staticmethod
    def _validate_parsers(p_list):
        """
        :param p_list: list of parsers to be valid instance
        :return:
        """
        if not(p_list, list):
            raise FieldException('Parsers must be list instance')

        for p in p_list:
            if not isinstance(p, BaseParser) or not issubclass(p.__class__, BaseParser):
                raise FieldException('Parsers must be BaseValidator instance/subclass')

