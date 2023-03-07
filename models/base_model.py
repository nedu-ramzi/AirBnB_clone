#!/usr/bin/python3
"""Defines the Basemodel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the base model for the project
        and defines all the common attributes/method for other classes.

        Args:
            id (str): assign with an uuid when an instance is created
            created_at: assigns the current datetime
            updated_at: updates the current datetime
    """

    def __init__(self, *args, **kwargs):
        """Intializes the public instance attribute
        Args:
            *args: unused argument
            **kwargs: Key/value pairs of attributes
        """
        dtformat = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, dtformat)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns the string representation of the class"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance dict
        """
        map_dict = self.__dict__.copy()
        map_dict["created_at"] = self.created_at.isoformat()
        map_dict["updated_at"] = self.updated_at.isoformat()
        map_dict["__class__"] = self.__class__.__name__
        return map_dict
