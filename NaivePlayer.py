from Player import Player
from Exceptions import FullBoardException


class NaivePlayer(Player):
    def play(self, board):
        """Play of NaivePlayer, trys to add domino according to order in hand"""
        for domino in self.hand:
            try:
                if board.add(domino):
                    self.hand.remove_domino(domino)
                    return True
                elif board.add(domino, add_to_right=False):
                    self.hand.remove_domino(domino)
                    return True
                # If board is full, return False
            except FullBoardException:
                return False
        return False

