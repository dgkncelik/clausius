from .exception import ValidatorError

class BaseValidator(object):
    @staticmethod
    def validate(value):
        return True