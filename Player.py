from Hand import Hand
from Domino import Domino
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, age, hand):
        """
        Constructor, Abstract class
        :param name: Name of player
        :param age: Age of player
        :param hand: The hand the player has
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """Score of the player, sum of values of each domino"""
        score = 0
        if isinstance(self.hand, Hand):
            for i in self.hand.array:
                score += i.get_right() + i.get_left()
        return score

    def has_dominoes(self):
        """Checks if player has any dominoes left in hand"""
        if len(self.hand) == 0:
            return False
        return True

    @abstractmethod
    def play(self, board):
        """Abstract method, implemented by inheritance"""
        pass

    def __str__(self):
        """Returns String of name, age, hand and score of player"""
        return f"Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}"

    def __repr__(self):
        """Representation of player when printing"""
        return str(self)

