from unittest import TestCase
from NaivePlayer import NaivePlayer
from MaxScorePlayer import MaxScorePlayer
from RandomPlayer import RandomPlayer
from Team import Team
from Board import Board
from Game import Game
from Domino import Domino
from Hand import Hand
import random

class TestGame(TestCase):
    def test_play(self):
        d1 = Domino(4, 6)
        d2 = Domino(2, 6)
        d3 = Domino(4, 4)
        p1 = NaivePlayer("Naivi", 26, Hand([d1]))
        p2 = MaxScorePlayer("Maxim", 26,Hand([d2]))
        p3 = RandomPlayer("RandiM", 26, Hand([d3]))
        p4 = RandomPlayer("Randi", 26, Hand([d1, d2]))
        p5 = NaivePlayer("Bro1", 26, Hand([d1]))
        p6 = NaivePlayer("Moe2", 26, Hand([d3]))
        t1 = Team("Blue", [p1, p2])
        t2 = Team("Red", [p3, p4])
        t3 = Team("Bros", [p5])
        t4 = Team("Moes", [p6])
        b1 = Board(2)
        b2 = Board(4)
        g1 = Game(b1, t1, t2)
        g2 = Game(b1, t2, t1)
        g3 = Game(b2, t3, t4)
        self.assertEqual('Team Blue wins Team Red', g1.play())
        self.assertEqual(str(b1), '[4|4][4|6]')
        self.assertEqual(8, t1.score_team())
        self.assertTrue(t1.has_dominoes_team())
        self.assertEqual(18, t2.score_team())
        self.assertTrue(t2.has_dominoes_team())
        self.assertEqual('Team Blue wins Team Red', g2.play())
        self.assertTrue(('Draw!' == g3.play()))
