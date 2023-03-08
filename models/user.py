#!/usr/bin/python3
"""Defines a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a class User that inherits fromm BaseModel

    Pubic Class Attributes:
        email (str): the user's email
        password (str): the user's password
        first_name (str): first name of the user
        last_name (str): last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
