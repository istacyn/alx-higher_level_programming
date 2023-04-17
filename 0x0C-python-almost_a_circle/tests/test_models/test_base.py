#!/usr/bin/python3


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_json_string(self):
        # Test empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test None argument
        self.assertEqual(Base.to_json_string(None), "[]")

        # Test list of dictionaries
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(type(json_string), str)

    def test_save_to_file(self):
        # Test None argument
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        # Test save to file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2], "filename.json")
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 81)

        # Test overwrite file
        r3 = Rectangle(5, 5)
        Rectangle.save_to_file([r3])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 50)

        # Test save Square to file
        s1 = Square(5)
        s2 = Square(10, 2, 1)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 70)

    def test_create(self):
        # Test create Rectangle instance
        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))

        # Test create Square instance
        s1 = Square(5)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))

    def test_load_from_file(self):
        # Test load Rectangle instances from file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(str(rectangles[0]), str(r1))
        self.assertEqual(str(rectangles[1]), str(r2))

        # Test load Square instances from file
        s1 = Square(5)
        s2 = Square(10, 2, 1)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(str(squares[0]), str(r1))
        self.assertEqual(str(squares[1]), str(r2))

        # Test for load from non-existent file
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    inittest.main()
