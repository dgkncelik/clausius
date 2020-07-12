import unittest
from tools.validator.integer import IntegerValidator
from tools.validator.exception import ValidatorError


class TestIntegerValidator(unittest.TestCase):
    def test_min_value(self):
        validator = IntegerValidator(min_value=15)
        value = 12
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = IntegerValidator(min_value=15)
        value = 20
        self.assertEqual(validator.validate(value), True)

    def test_max_value(self):
        validator = IntegerValidator(max_value=40)
        value = 100
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = IntegerValidator(max_value=40)
        value = 39
        self.assertEqual(validator.validate(value), True)

    def test_validate(self):
        validator = IntegerValidator(min_value=20, max_value=70)
        value = 2.71
        self.assertRaises(ValidatorError, validator.validate, value)

        value = None
        self.assertRaises(ValidatorError, validator.validate, value)

        value = 'abcde'
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = IntegerValidator(min_value=10, max_value=70)
        value = 40
        self.assertEqual(validator.validate(value), True)


if __name__ == '__main__':
    unittest.main()

