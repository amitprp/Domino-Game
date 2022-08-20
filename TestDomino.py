from unittest import TestCase
from Domino import Domino
from Exceptions import InvalidNumberException


class TestDomino(TestCase):
    def setUp(self):
        self.d1 = Domino(1, 2)
        self.d2 = Domino(2, 1)
        self.d3 = Domino(3, 0)
        self.d4 = Domino(4, 6)

    def test__init__(self):
        try:
            d5 = Domino(0, 7)
        except InvalidNumberException as e:
            print(f"{e} Number too big for domino")
        try:
            d6 = Domino(-1, 6)
        except InvalidNumberException as e1:
            print(f"{e1} Number too small for domino")

    def test_get_left(self):
        self.assertEqual(1, self.d1.get_left(), msg="get_left_func: Error in get left")
        print(self.d1.get_left())
        self.assertFalse(2 == self.d1.get_left(), msg="get_left_func: Error, get left gives right")

    def test_get_right(self):
        self.assertEqual(0, self.d3.get_right(), msg="get_right_func: Error in get right")
        self.assertFalse(3 == self.d3.get_right(), msg="get_right_func: Error, get right gives left")

    def test__str__(self):
        self.assertEqual('[4|6]', str(self.d4), msg="str_func: Error in str")

    def test__eq__(self):
        self.assertTrue(self.d1 == self.d2, msg="eq_func: Error in equalizing")

    def test__ne__(self):
        self.assertFalse(self.d1 != self.d2, msg="ne_func: Error, giving not even when even")
        self.assertTrue(self.d1 != self.d4, msg="ne_func: Error in not even")

    def test__gt__(self):
        self.assertTrue(self.d4 > self.d1, msg="gt_func:Error in checking gt")
        self.assertFalse(self.d1 > self.d2, msg="gt_func: Error, equal not gt")

    def test_flip(self):
        d4_flip = self.d4.flip()
        self.assertTrue(d4_flip.get_left() == 6 and d4_flip.get_right() == 4, msg="flip_func: Error in flipping tile")

    def test__contains__(self):
        self.assertIn(2, self.d1, msg="contains_func: Error")
        self.assertNotIn(5, self.d1)

    def test__repr__(self):
        self.assertEqual(str(self.d4), self.d4.__repr__(), msg="Error in repr")
