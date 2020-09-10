import unittest
from unittest.mock import MagicMock
from model.field.base_field import BaseField
from tools.validator.base_validator import BaseValidator
from tools.parser.base_parser import BaseParser


class TestBaseField(unittest.TestCase):
    def test_validate(self):
        validator1 = BaseValidator()
        validator2 = BaseValidator()
        validator3 = BaseValidator()
        validators = [validator1, validator2, validator3]

        field = BaseField()
        field.validators = validators

        self.assertEqual(field.validate(), True)

        validator4 = BaseValidator()
        validator5 = BaseValidator()
        validator6 = BaseValidator()
        validator4.validate = MagicMock()
        validator5.validate = MagicMock()
        validator6.validate = MagicMock()
        validators2 = [validator4, validator5, validator6]

        field2 = BaseField()
        field2.validators = validators2
        field2.validate()

        self.assertEqual(validator4.validate.called, True)
        self.assertEqual(validator5.validate.called, True)
        self.assertEqual(validator6.validate.called, True)

    def test_parse(self):
        parser1 = BaseParser()
        parser2 = BaseParser()
        parser3 = BaseParser()
        parsers = [parser1, parser2, parser3]

        field = BaseField()
        field.key = 'TEST_KEY'
        field.value = 'TEST_VALUE'
        field.parsers = parsers

        self.assertEqual(field.parse(), ['TEST_VALUE', 'TEST_VALUE', 'TEST_VALUE'])

        parser4 = BaseParser()
        parser5 = BaseParser()
        parser6 = BaseParser()
        parser4.parse = MagicMock()
        parser5.parse = MagicMock()
        parser6.parse = MagicMock()
        parsers2 = [parser4, parser5, parser6]

        field2 = BaseField()
        field2.parsers = parsers2
        field2.key = 'TEST'
        field2.value = 'TEST'
        field2.parse()

        self.assertEqual(parser4.parse.called, True)
        self.assertEqual(parser5.parse.called, True)
        self.assertEqual(parser6.parse.called, True)

    def test_get_validators(self):
        validator1 = BaseValidator()
        validator2 = BaseValidator()
        validator3 = BaseValidator()

        field = BaseField()
        validators = [validator1, validator2, validator3]
        field._validators = validators
        self.assertEqual(field.validators, validators)

    def test_set_validators(self):
        validator1 = BaseValidator()
        validator2 = BaseValidator()
        validator3 = BaseValidator()

        field = BaseField()
        validators = [validator1, validator2, validator3]
        field.validators = validators
        self.assertEqual(field._validators, validators)

    def test_get_parsers(self):
        parser1 = BaseParser()
        parser2 = BaseParser()
        parse3 = BaseParser()

        field = BaseField()
        parsers = [parser1, parser2, parse3]
        field._parsers = parsers
        self.assertEqual(field.parsers, parsers)

    def test_set_parsers(self):
        parser1 = BaseParser()
        parser2 = BaseParser()
        parser3 = BaseParser()

        field = BaseField()
        parsers = [parser1, parser2, parser3]
        field.parsers = parsers
        self.assertEqual(field._parsers, parsers)

    def test_set_key(self):
        # TODO: complete test
        pass

    def test_get_key(self):
        pass

    def test_set_value(self):
        pass

    def test_get_value(self):
        pass

    def test__validate_validators(self):
        pass

    def test__validate_parsers(self):
        pass


if __name__ == '__main__':
    unittest.main()
