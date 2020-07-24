import unittest
from tools.validator.test.test_base_validator import TestBaseValidator
from tools.validator.test.test_bool import TestBoolValidator
from tools.validator.test.test_dictionary import TestDictionaryValidator
from tools.validator.test.test_list import TestListValidator
from tools.validator.test.test_float import TestFloatValidator
from tools.validator.test.test_integer import TestIntegerValidator
from tools.validator.test.test_string import TestStringValidator


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBaseValidator('test_validate'))
    suite.addTest(TestBoolValidator('test_validate'))
    suite.addTest(TestDictionaryValidator('test_min_length'))
    suite.addTest(TestDictionaryValidator('test_max_length'))
    suite.addTest(TestDictionaryValidator('test_validate'))
    suite.addTest(TestListValidator('test_min_length'))
    suite.addTest(TestListValidator('test_max_length'))
    suite.addTest(TestListValidator('test_validate'))
    suite.addTest(TestFloatValidator('test_min_value'))
    suite.addTest(TestFloatValidator('test_min_value'))
    suite.addTest(TestFloatValidator('test_validate'))
    suite.addTest(TestIntegerValidator('test_min_value'))
    suite.addTest(TestIntegerValidator('test_min_value'))
    suite.addTest(TestIntegerValidator('test_validate'))
    suite.addTest(TestStringValidator('test_min_length'))
    suite.addTest(TestStringValidator('test_max_length'))
    suite.addTest(TestStringValidator('test_whitespace'))
    suite.addTest(TestStringValidator('test_validate'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
