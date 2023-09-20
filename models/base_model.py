#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            current_time = datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            storage.new(self)
        else:
            # Check if 'created_at' and 'updated_at' keys are missing in kwargs
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now().isoformat()

            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now().isoformat()

            # Use pop method with a default value to delete '__class__' key
            kwargs.pop('__class__', None)

            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at']
                    , '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at']
                    , '%Y-%m-%dT%H:%M:%S.%f')
            
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
