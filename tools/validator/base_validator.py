"""
Base validator class
Validators aim to validate data with validate(value) method
Validation parameters must be given on init

ex:

BaseValidator(arg1=value1, arg2=value2, ...).validate(value)
"""


class BaseValidator(object):
    def __init__(self, **kwargs):
        self._initial_parameters = kwargs

    def validate(self, value, **kwargs):
        """
        :param value: data which will process to validate
        :return: True on validated data
        :raise: ValidatorError exception on non validated data
        """
        return True
