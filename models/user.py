#!/usr/bin/python3
"""model for the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from the BaseModel class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
