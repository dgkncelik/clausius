import unittest
from tools.validator.base_validator import BaseValidator


class TestBaseValidator(unittest.TestCase):
    def test_validate(self):
        validator = BaseValidator()
        value = None
        self.assertEqual(validator.validate(value), True)

        value = ''
        self.assertEqual(validator.validate(value), True)

        value = '123123'
        self.assertEqual(validator.validate(value), True)

        value = 123123
        self.assertEqual(validator.validate(value), True)


if __name__ == '__main__':
    unittest.main()
