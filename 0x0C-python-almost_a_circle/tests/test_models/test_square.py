#!/usr/bin/python3


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(7, 2, 3, 8)
        self.assertEqual(s2.id, 8)
        self.assertEqual(s2.size, 7)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

        with self.assertRaises(TypeError):
            s3 = Square("not a number")
        with self.assertRaises(ValueError):
            s4 = Square(-10)

        def test_str(self):
            s1 = Square(4, 2, 1, 12)
            self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")

        def test_update(self):
            s1 = Square(2, 2, 2, 2)
            s1.update(3)
            self.assertEqual(str(s1), "[Square] (3) 2/2 - 2")
            s1.update(4, 3)
            self.assertEqual(str(s1), "[Square] (4) 2/2 - 3")
            s1.update(5, 4, 5)
            self.assertEqual(str(s1), "[Square] (5) 5/2 - 4")
            s1.update(y=6, size=7, id=6, x=7)
            self.assertEqual(str(s1), "[Square] (6) 7/6 - 7")

        def test_to_dictionary(self):
            s1 = Square(3, 1, 2, 5)
            self.asserEqual(s1.to_dictionary(),
                            {'id': 5, 'size': 3, 'x': 1, 'y': 2})


if __name__ == '__main__':
    unittest.main()
