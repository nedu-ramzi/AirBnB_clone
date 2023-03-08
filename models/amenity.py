#!/usr/bin/python3
"""Defines the Class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a class Amenity that inherits from BaseModel

    Args:
        name (str): name of the amenity
    """

    name = ""
