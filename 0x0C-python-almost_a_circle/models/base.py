#!/usr/bin/python3
"""This module creates a base class for
all other classes in this project"""


import json
import csv
import turtle


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.

        Args:
        list_objs (list): A list of objects to save.

        Returns:
        None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of objects from a CSV file.

        Returns:
        A list of objects loaded from the file.
        An empty list if the file does not exist or is empty
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.

        Args:
        list_rectangles (list): A list of Rectangle objects to draw.
        list_squares (list): A list of Square objects to draw.
        """
        window = turtle.Screen()
        window.bgcolor("white")

        # cretae a turtle to draw the shapes
        t = turtle.Turtle
        t.pensize(5)
        t.shape("turtle")
        t.color("red")

        # draw rectangle shape
        for r in list_rectangles:
            t.penup()
            t.goto(r.x, r.y)
            t.pendown()
            t.setheading(0)
            t.forward(r.width)
            t.left(90)
            t.forward(r.height)
            t.left(90)
            t.forward(r.width)
            t.left(90)
            t.forward(r.height)
            t.left(90)

        # draw square shape
        for s in list_squares:
            t.penup()
            t.goto(s.x, s.y)
            t.pendown()
            t.setheading(0)
            t.forward(r.size)
            t.left(90)
            t.forward(r.size)
            t.left(90)
            t.forward(r.size)
            t.left(90)
            t.forward(r.size)
            t.left(90)

        turtle.exitonclick()
