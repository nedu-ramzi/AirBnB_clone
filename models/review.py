#!/usr/bin/python3
"""Defines a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a class review that inherits from a basemodel
    Args:
        place_id (str): the place id
        user_id (str): the user id
        text (str): the review text
    """

    place_id = ""
    user_id = ""
    text = ""
