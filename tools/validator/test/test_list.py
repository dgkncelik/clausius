import unittest
from tools.validator.list import ListValidator
from tools.validator.exception import ValidatorError


class TestListValidator(unittest.TestCase):
    def test_min_length(self):
        validator = ListValidator(min_length=5)
        value = [1, 2, 3, 4]
        self.assertRaises(ValidatorError, validator.validate, value)

        value = [1, 2, 3, 4, 5]
        self.assertEqual(validator.validate(value), True)

    def test_max_length(self):
        validator = ListValidator(max_length=6)
        value = [1, 2, 3, 4, 5, 6, 7]
        self.assertRaises(ValidatorError, validator.validate, value)

        value = [1, 2, 3, 4, 5]
        self.assertEqual(validator.validate(value), True)

    def test_validate(self):
        validator = ListValidator(min_length=4, max_length=7)
        value = [1, 2, 3, 4, 5]
        self.assertEqual(validator.validate(value), True)

        value = ''
        self.assertRaises(ValidatorError, validator.validate, value)

        value = None
        self.assertRaises(ValidatorError, validator.validate, value)

        value = True
        self.assertRaises(ValidatorError, validator.validate, value)

        value = 123123
        self.assertRaises(ValidatorError, validator.validate, value)

        value = {}
        self.assertRaises(ValidatorError, validator.validate, value)


if __name__ == '__main__':
    unittest.main()
