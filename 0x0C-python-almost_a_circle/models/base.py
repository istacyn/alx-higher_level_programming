#!/usr/bin/python3
"""This module creates a base class for
all other classes in this project"""


import json


class Base:
    """
    Base class for creating objects with unique ids.

    Attributes:
    __nb_objects: Keeps track of number of instances created and
    assigns unique id to them.

    id: Holds unique id for ech instance of the class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The constructor for the Base class.

        Args:
        id (int): The id assigned to the instance.
        If not provided, unique id will be generated using
        __nb_objects attribute.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string"""
        if not json_string:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ = ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_str = file.read()
                obj_list = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in obj_list]
        except FileNotFoundError:
            return []
