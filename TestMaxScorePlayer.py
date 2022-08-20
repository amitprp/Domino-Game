from unittest import TestCase
from Domino import Domino
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer
from Board import Board


class TestMaxScorePlayer(TestCase):
    def setUp(self):
        self.d1 = Domino(4, 6)
        self.d2 = Domino(6, 6)
        self.d3 = Domino(5, 6)
        self.d4 = Domino(3, 6)
        self.d5 = Domino(2, 1)
        self.h1 = Hand([self.d5, self.d3, self.d2, self.d4])
        self.b1 = Board(6)
        self.b1.add(self.d1)
        self.b2 = Board(1)
        self.b2.add(self.d1)
        self.p1 = MaxScorePlayer('Amit', 25, self.h1)
        self.p2 = MaxScorePlayer('Amit', 25, Hand([self.d1]))
    def test_play(self):
        self.p1.play(self.b1)
        self.assertTrue(self.b1[1] == self.d2)
        self.p1.play(self.b1)
        self.assertFalse(self.p1.play(self.b1))
        self.assertFalse(self.p2.play(self.b2))
    def test__str__(self):
        self.assertEqual(
            f"Name: Amit, Age: 25, Hand: {Hand(sorted(self.h1.array, reverse=True))}, Score: 35, I can win the game!",
            str(self.p1))

