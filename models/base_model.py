#!/usr/bin/python3
"""Documentation for the BaseModel class
"""

import uuid
import json
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes
    on the Airbnb clone project
    """

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel objects"""

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        date_format = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.strptime(value, date_format)
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class"""

        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """

        createdTime = self.created_at.isoformat()
        updatedTime = self.updated_at.isoformat()
        class_name = self.__class__.__name__
        our_dict = self.__dict__
        our_dict["__class__"] = class_name
        our_dict["created_at"] = createdTime
        our_dict["updated_at"] = updatedTime
        return our_dict
