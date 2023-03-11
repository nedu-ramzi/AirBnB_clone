#!/usr/bin/python3
"""Defines a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a class City that inherits from BaseModel

    Args:
        state_id (Str) - id of the state
        name (str) - name of the city
    """

    state_id = ""
    name = ""
