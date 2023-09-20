#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage or filtered by class"""
        if cls is None:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def delete(self, obj=None):
        """Deletes obj from storage if it exists"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def save(self):
        """Saves storage dictionary to file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, obj_dict in serialized_objects.items():
                    class_name = obj_dict['__class__']
                    if class_name in classes:
                        obj = classes[class_name](**obj_dict)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass

