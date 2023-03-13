#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represents a class that that serializes instances to a JSON file
        and deserializes JSON file to instances

        Private class attributes:
            __file_path: string - path to the json file to save objects to
            __objects: dictionary - empty but will store all objects by
                <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        obj - object to write
        """
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: value.to_dict()
                      for key, value in FileStorage.__objects.items()}, f)

    def reload(self):
        """deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dictobj = json.load(f)
                for value in dictobj.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except FileNotFoundError:
            pass
