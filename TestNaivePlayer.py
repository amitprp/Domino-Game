from unittest import TestCase
from Domino import Domino
from Board import Board
from NaivePlayer import NaivePlayer
from Hand import Hand


class TestNaivePlayer(TestCase):
    def test_play(self):
        d1 = Domino(4, 6)
        d2 = Domino(3, 6)
        d3 = Domino(2, 4)
        d4 = Domino(1, 1)
        h1 = Hand([d2, d3])
        b1 = Board(4)
        b2 = Board(1)
        p1 = NaivePlayer('Amit', 25, h1)
        p2 = NaivePlayer('Amit', 25, Hand([d1]))
        b1.add(d1)
        self.assertTrue(p1.play(b1))
        self.assertTrue(p1.play(b1))
        self.assertFalse(p1.play(b1))
        b2.add(d1)
        self.assertFalse(p2.play(b2))

