from Exceptions import FullBoardException


class Game:
    def __init__(self, board, team1, team2):
        """
        Constructor
        :param board: Board that the game occurs in
        :param team1: Team 1 of the game
        :param team2: Team 2 of the game
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """
        Play function.
        Each team plays in it's turn, if succeeded or not, the turn goes to the other team.
        When no more plays left, the game is over.
        A team wins when they have less points, Draw returns when they have the same score
        :return: A string representing the winning team
        """
        team1_play = True
        team2_play = True
        while team1_play != False and team2_play != False:
            # If team 1 doesn't have any dominoes left to play with
            if not self.team1.has_dominoes_team:
                break
            team1_play = self.team1.play(self.board)
            # If team 2 doesn't have any dominoes left to play with
            if not self.team2.has_dominoes_team:
                break
            team2_play = self.team2.play(self.board)
        # Picking winner
        if self.team1.score_team() < self.team2.score_team():
            return f"Team {self.team1.name} wins Team {self.team2.name}"
        elif self.team2.score_team() < self.team1.score_team():
            return f"Team {self.team2.name} wins Team {self.team1.name}"
        return "Draw!"
