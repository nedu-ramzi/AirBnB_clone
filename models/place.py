#!/usr/bin/python3
"""Defines a class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the class Place that inherits from BaseModel
    Args:
        city_id (str): id of the city
        user_id (str): id of the user
        name (Str): name of the place
        description (str): description of the place
        number_rooms (int): no of rooms
        number_bathrooms (int): no of bathrooms
        max_guest (int): maximum amount of guest
        price_by_night (int) - price of the room per night
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amentity_ids (list): list of the amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
