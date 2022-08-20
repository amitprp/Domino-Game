from unittest import TestCase
from Domino import Domino
from Hand import Hand
from Player import Player
from NaivePlayer import NaivePlayer

class TestPlayer(TestCase):
    def setUp(self):
        self.d1 = Domino(4, 6)
        self.hand1 = Hand([self.d1])
        self.p1 = NaivePlayer('Yehiel', 25, self.hand1)
        self.p2 = NaivePlayer('Amit', 25, Hand([]))

    def test_abstract(self):
        self.assertRaises(TypeError, Player.__init__, 'Yehiel', 25, self.hand1)

    def test_score(self):
        self.assertEqual(10, self.p1.score())

    def test_has_dominoes(self):
        self.assertTrue(self.p1.has_dominoes())
        self.assertFalse(self.p2.has_dominoes())

    def test__str__(self):
        self.assertEqual(f"Name: Yehiel, Age: 25, Hand: [4|6], Score: 10", str(self.p1))

    def test__repr(self):
        self.assertTrue(str(self.p1) == self.p1.__repr__())