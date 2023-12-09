#!/usr/bin/python3
"""FileStorage class module
"""

import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """

        className = obj.__class__.__name__
        obj_id = obj.id
        obj_key = "{}.{}".format(className, obj_id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        FilePath = FileStorage.__file_path
        with open(FilePath, 'w', encoding='utf-8') as f:
            objects_dict = {}
            for key, value in FileStorage.__objects.items():
                objects_dict[key] = value.to_dict()
            json.dump(objects_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        """

        from models.base_model import BaseModel
        # from models.user import User
        # from models.place import Place
        # from models.state import State
        # from models.city import City
        # from models.amenity import Amenity
        # from models.review import Review

        classes = {'BaseModel': BaseModel}
        """classes = {
                    'BaseModel' : BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                   }"""

        if os.path.exists(FileStorage.__file_path):
            obj_dict = {}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)

            for key, value in obj_dict.items():
                class_name = value['__class__']
                self.all()[key] = classes[class_name](**value)
