import unittest
from tools.validator.bool import BoolValidator
from tools.validator.exception import ValidatorError


class TestBoolValidator(unittest.TestCase):
    def test_validate(self):
        validator = BoolValidator()
        value = 'abcdefgh'
        self.assertRaises(ValidatorError, validator.validate, value)

        validator = BoolValidator()
        value = True
        self.assertEqual(validator.validate(value), True)

        value = False
        self.assertEqual(validator.validate(value), True)


if __name__ == '__main__':
    unittest.main()
