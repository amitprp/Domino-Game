from Player import Player
from Hand import Hand
from Exceptions import FullBoardException

class MaxScorePlayer(Player):
    def __init__(self, name, age, hand):
        """
        Constructor using Player
        :param name: Name of player
        :param age: Age of player
        :param hand: Hand of the player
        """
        # Sorting hand according to score, maximizing value in hand
        hand = Hand(sorted(hand.array, reverse=True))
        super().__init__(name, age, hand)

    def play(self, board):
        """Play of MaxScorePlayer, trys to add domino from start of hand to the end"""
        for domino in self.hand:
            try:
                if board.add(domino):
                    self.hand.remove_domino(domino)
                    return True
                elif board.add(domino, add_to_right=False):
                    self.hand.remove_domino(domino)
                    return True
            # When Full board, return False
            except FullBoardException:
                return False
        return False

    def __str__(self):
        """String of MaxScorePlayer, with Player string"""
        return f"{super().__str__()}, I can win the game!"



