from unittest import TestCase
from Board import Board
from Exceptions import InvalidNumberException, EmptyBoardException, FullBoardException
from Domino import Domino


class TestBoard(TestCase):
    def setUp(self):
        self.b1 = Board(5)
        self.b2 = Board(6)
        self.d1 = Domino(4, 6)
        self.d2 = Domino(3, 0)
        self.d3 = Domino(6, 4)
        self.b2.add(self.d1)
        self.b2.add(self.d2)
        self.b3 = Board(4)
        self.b3.add(self.d1)
        self.b4 = Board(4)
        self.b4.add(self.d1)

    def test__init__(self):
        self.assertRaises(InvalidNumberException, Board, 29)
        self.assertRaises(InvalidNumberException, Board, 0)
        self.assertTrue([] == self.b1.array, msg="init_func:Error in array constructor")

    def test_in_left(self):
        with self.assertRaises(EmptyBoardException):
            self.b1.in_left()
        self.assertEqual(self.d1.get_left(), self.b2.in_left())

    def test_in_right(self):
        with self.assertRaises(EmptyBoardException):
            self.b1.in_right()
        self.b2.add(self.d3)
        self.assertEqual(self.d3.get_right(), self.b2.in_right())

    def test_add(self):
        self.b1.add(self.d1)
        self.b1.add(self.d3, False)
        self.b1.add(Domino(2, 6), False)
        b1 = Board(1)
        b1.add(Domino(4, 6))
        self.assertEqual(self.d1, self.b1[len(self.b1.array)-1], msg="add_func: Error in adding to right when True")
        self.assertEqual(self.d3, self.b1[1], msg="add_func: Error in adding to left when False")
        self.assertEqual(Domino(2, 6), self.b1[0], msg="add_func: Error in adding to equal domino")
        self.assertRaises(FullBoardException, b1.add, self.d2)
        self.b1.add(self.d1)
        self.assertEqual(self.d1.flip().get_right(), self.b1.in_right())
        self.b1.add(Domino(2, 3), False)
        self.assertEqual((Domino(3,2).get_left()), self.b1.in_left())

    def test__getitem__(self):
        self.assertEqual(self.d1, self.b2[0], msg="get_item_func: Error")

    def test__contains__(self):
        self.b1.add(self.d1)
        self.assertIn(self.d1, self.b1, msg="contains_func: Error")

    def test__eq__(self):
        b1 = Board(4)
        b1.add(self.d3)
        self.assertTrue(self.b3 == self.b4, msg="eq_func: Error in equalizing boards")
        self.assertFalse(self.b3 == b1)
        self.assertFalse(self.b1 == self.b2)

    def test__ne__(self):
        self.assertFalse(self.b3 != self.b4, msg="ne_func: Error in not equalizing equal boards")

    def test__len__(self):
        self.assertTrue(1 == len(self.b3), msg="len_func: Error in length of board")

    def test__str__(self):
        self.assertEqual('[4|6]', str(self.b3), msg="str_func: Error in making string")

    def test__repr__(self):
        self.assertEqual('[4|6]', self.b3.__repr__(), msg="repr_func: Error in printing")
