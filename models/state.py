#!/usr/bin/python3
"""Defines a state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a class State that inherits a BaseModel

    Args:
        name (str) - name of the state
    """

    name = ""
