#!/usr/bin/python3


import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        # Test valid arguments
        r = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 1)

        # Test invalid width
        with self.assertRaises(ValueError):
            r = Rectangle(0, 20, 30, 40, 1)

        # Test invalid height
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0, 30, 40, 1)

        # Test invalid x_coordinate
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -30, 40, 1)

        # Test invalid y-coordinate
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 30, -40, 1)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

        with self.assertRaises(TypeError):
            r = Rectangle(10, "20")
            r.area()

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r.display()
            self.assertEqual(fakeOutput.getvalue(), expected_output)

        with self.assertRaises(TypeError):
            r = Rectangle(3, "2")
            r.display()

    def test_update(self):
        r = Rectangle(10, 20, 30, 40, 1)
        r.update(2, 20, 30, 40, 50)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)
        self.assertEqual(r.id, 2)

        r.update(3, 30)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)
        self.assertEqual(r.id, 3)

        with self.assertRaises(TypeError):
            r.update(4, "30")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 20, 30, 40, 1)
        r1_dict = {'id': 1, 'width': 10, 'height': 20, 'x': 30, 'y': 40}
        self.assertDictEqual(r1.to_dictionary(), r1_dict)


if __name__ == '__main__':
    unittest.main()
