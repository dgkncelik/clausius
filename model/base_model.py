from .expception import ModelInitilzationError
from clausius.storage import BaseStorage
from clausius.messanger import BaseMessanger

class BaseModel(object):
    def __init__(self, storage=BaseStorage(), messanger=BaseMessanger(), initial_data=dict()):
        if not isinstance(storage, BaseStorage):
            raise ModelInitilzationError()

        if not isinstance(messanger, BaseMessanger):
            raise ModelInitilzationError()

        if not initial_data and not isinstance(initial_data, dict):
            raise ModelInitilzationError()
        
        self.storage = storage
        self.messanger = messanger
        self.initial_data = initial_data

    def save(self, **kwargs):
        return self.storage.save(self, **kwargs)
    
    def delete(self, **kwargs):
        return self.storage.delete(self, **kwargs)
    
    def update(self, **kwargs):
        return self.storage.update(self, **kwargs)

    def get(self, kwargs):
        return self.storage.get(self, **kwargs)

    def filter(self, kwargs):
        return self.storage.filter(self, **kwargs)

    def send(self, kwargs):
        return self.messanger.send(self, **kwargs)

    def receive(self, kwargs):
        return self.messanger.receive(self, **kwargs)
    
    def validate(self):
        pass

    def compose(self):
        pass
