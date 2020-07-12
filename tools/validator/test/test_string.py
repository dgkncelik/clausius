import unittest
from tools.validator.string import StringValidator
from tools.validator.exception import ValidatorError


class TestStringValidator(unittest.TestCase):
    def test_min_length(self):
        validator = StringValidator(min_length=10)
        value = 'abcefghij'
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = StringValidator(min_length=15)
        value = 'abcdefghijklmnoprstuvyxzw'
        self.assertEqual(validator.validate(value), True)

    def test_max_length(self):
        validator = StringValidator(max_length=1)
        value = 'ab'
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = StringValidator(max_length=100)
        value = 'abcd'
        self.assertEqual(validator.validate(value), True)

    def test_whitespace(self):
        validator = StringValidator(whitespace=False)
        value = '        \n\t\r'
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = StringValidator(whitespace=True)
        self.assertEqual(validator.validate(value), True)

    def test_validate(self):
        validator = StringValidator(min_length=4, max_length=10, whitespace=False)
        value = '     '
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = StringValidator()
        value = None
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = StringValidator()
        value = 123
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = StringValidator(min_length=10, max_length=45)
        value = '123456789012345678901234567890abcdefg\t\n\r'
        self.assertEqual(validator.validate(value), True)


if __name__ == '__main__':
    unittest.main()
