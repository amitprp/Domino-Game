import random
from Player import Player
from Exceptions import FullBoardException
import copy


class RandomPlayer(Player):
    def play(self, board):
        """Play of RandomPlayer
            Shuffles hand randomly and then trys to add in order of dominoes in hand
             if added, removes domino from hand"""
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        rand_hand = copy.deepcopy(self.hand.array)
        random.shuffle(rand_hand)
        for domino in rand_hand:
            try:
                if board.add(domino):
                    self.hand.remove_domino(domino)
                    return True
                elif board.add(domino, add_to_right=False):
                    self.hand.remove_domino(domino)
                    return True
            # if Board is full, returns False
            except FullBoardException:
                return False
        return False

