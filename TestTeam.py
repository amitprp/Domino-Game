from unittest import TestCase
from Team import Team
from NaivePlayer import NaivePlayer
from RandomPlayer import RandomPlayer
from MaxScorePlayer import MaxScorePlayer
from Domino import Domino
from Hand import Hand
from Board import Board


class TestTeam(TestCase):
    def setUp(self):
        self.d1 = Domino(4, 6)
        self.d2 = Domino(3, 2)
        self.d3 = Domino(3, 6)
        self.d4 = Domino(2, 1)
        self.d5 = Domino(4, 4)
        self.b1 = Board(4)
        self.b1.add(self.d5)
        self.h1 = Hand([self.d1, self.d2]) #Score: 15
        self.h2 = Hand([self.d3, self.d4]) #Score: 12
        self.h3 = Hand([self.d1, self.d4]) #Score: 13
        self.max1 = MaxScorePlayer("Maxim", 25, self.h1)
        self.rand1 = RandomPlayer("Randi", 25, self.h2)
        self.naiv1 = NaivePlayer("Naivi", 25, self.h3)
        self.noplaysplayer = MaxScorePlayer("Nada", 25, Hand([]))
        self.t1 = Team('Red', [self.max1, self.rand1, self.naiv1]) #Score: 40
        self.t2 = Team('MaxTeam', [self.noplaysplayer])
    def test_get_team(self):
        list_of_players = [self.max1, self.rand1, self.naiv1]
        players_index = 0
        for player in self.t1.get_team():
            self.assertEqual(str(list_of_players[players_index]), str(player))
            players_index += 1

    def test_score_team(self):
        self.assertEqual(40, self.t1.score_team())
        self.t1.play(self.b1)
        self.assertEqual(30, self.t1.score_team())

    def test_has_dominoes_team(self):
        self.assertTrue(self.t1.has_dominoes_team())
        self.assertFalse(self.t2.has_dominoes_team())


    def test_play(self):
        self.assertTrue(self.t1.play(self.b1))
        self.assertFalse(self.t2.play(self.b1))

    def test__str__(self):
        self.assertTrue(str(self.t1) == "Name Red, Score team: 40, Players: "
                                        "Name: Maxim, Age: 25, Hand: [4|6][3|2], Score: 15, I can win the game! "
                                        "Name: Randi, Age: 25, Hand: [3|6][2|1], Score: 12 "
                                        "Name: Naivi, Age: 25, Hand: [4|6][2|1], Score: 13")

