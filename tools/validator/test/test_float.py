import unittest
from tools.validator.float import FloatValidator
from tools.validator.exception import ValidatorError


class TestFloatValidator(unittest.TestCase):
    def test_min_value(self):
        validator = FloatValidator(min_value=15.271)
        value = 12
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = FloatValidator(min_value=15.271)
        value = 20.0271
        self.assertEqual(validator.validate(value), True)

    def test_max_value(self):
        validator = FloatValidator(max_value=40.0)
        value = 40.01
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = FloatValidator(max_value=40.0)
        value = 39.9
        self.assertEqual(validator.validate(value), True)

    def test_validate(self):
        validator = FloatValidator(min_value=20.0, max_value=70.0)
        value = 2
        self.assertRaises(ValidatorError, validator.validate, value)

        value = None
        self.assertRaises(ValidatorError, validator.validate, value)

        value = 'abcde'
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = FloatValidator(min_value=10.312, max_value=70.271)
        value = 40.169
        self.assertEqual(validator.validate(value), True)


if __name__ == '__main__':
    unittest.main()

