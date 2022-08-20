from unittest import TestCase
from Domino import Domino
from Hand import Hand
from Exceptions import NoSuchDominoException

class TestHand(TestCase):
    def setUp(self):
        self.d1 = Domino(3, 0)
        self.d2 = Domino(4, 6)
        self.d3 = Domino(2, 5)
        self.hand1 = Hand([self.d1])
        self.hand3 = Hand([self.d3])
    def test_add(self):
        self.hand1.add(self.d2)
        self.assertEqual(self.d2, self.hand1[1])
        self.hand1.add(self.d3, 1)
        self.assertEqual(self.d3, self.hand1[1])

    def test_remove_domino(self):
        self.assertEqual(0, self.hand1.remove_domino(self.d1))
        self.assertRaises(NoSuchDominoException, self.hand1.remove_domino, self.d2)

    def test__eq__(self):
        self.hand2 = Hand([self.d1])
        self.assertEqual(self.hand1, self.hand2)
        self.assertFalse(self.hand1 == self.hand3)

    def test__ne__(self):
        self.assertTrue(self.hand1 != self.hand3)
        self.assertFalse(self.hand1 != self.hand1)
