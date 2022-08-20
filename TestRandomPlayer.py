from unittest import TestCase
from Domino import Domino
from Hand import Hand
from RandomPlayer import RandomPlayer
from Board import Board


class TestRandomPlayer(TestCase):
    def test_play(self):
        d1 = Domino(4, 6)
        d2 = Domino(3, 6)
        d3 = Domino(2, 1)
        d4 = Domino(1, 0)
        d5 = Domino(5, 2)
        h1 = Hand([d2, d3, d4, d5])
        b1 = Board(4)
        b2 = Board(1)
        b2.add([d1])
        p1 = RandomPlayer('Amit', 25, h1)
        p2 = RandomPlayer('Amit', 25, Hand([d1]))
        b1.add(d1)
        self.assertTrue(p1.play(b1))
        self.assertFalse(p1.play(b1))
        self.assertTrue(h1 == p1.hand)
        self.assertFalse(p2.play(b2))
