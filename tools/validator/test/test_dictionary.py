import unittest
from tools.validator.dictionary import DictionaryValidator
from tools.validator.exception import ValidatorError


class TestDictionaryValidator(unittest.TestCase):
    def test_min_length(self):
        validator = DictionaryValidator(min_length=5)
        value = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertRaises(ValidatorError, validator.validate, value)

        value = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(validator.validate(value), True)

    def test_max_length(self):
        validator = DictionaryValidator(max_length=6)
        value = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'h': 7}
        self.assertRaises(ValidatorError, validator.validate, value)

        value = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(validator.validate(value), True)

    def test_validate(self):
        validator = DictionaryValidator(min_length=4, max_length=7)
        value = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
        self.assertEqual(validator.validate(value), True)

        value = ''
        self.assertRaises(ValidatorError, validator.validate, value)

        value = None
        self.assertRaises(ValidatorError, validator.validate, value)

        value = True
        self.assertRaises(ValidatorError, validator.validate, value)

        value = 123123
        self.assertRaises(ValidatorError, validator.validate, value)

        value = []
        self.assertRaises(ValidatorError, validator.validate, value)


if __name__ == '__main__':
    unittest.main()
