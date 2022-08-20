import copy


class Team:
    def __init__(self, name, players):
        """
        Constructor
        :param name: Name of team
        :param players: List of players in the team
        """
        self.name = name
        self.__players = players

    def get_team(self):
        """Function for getting players of team"""
        return copy.deepcopy(self.__players)

    def score_team(self):
        """Team score as implemented in domino"""
        team_score = 0
        for player in self.__players:
            # Score for each player
            team_score += player.score()
        return team_score

    def has_dominoes_team(self):
        """
        Function that checks if atleast 1 player has dominoes left
        :return: True if there's a player with dominoes, False otherwise
        """
        for player in self.get_team():
            if player.has_dominoes():
                return True
        return False

    def play(self, board):
        """Function of play for players in the team"""
        for player in self.__players:
            if player.play(board):
                return True
        return False

    def __str__(self):
        """
        Representing the team in a string, name and players
        :return: The name, score and the players in the team as a string
        """
        team_string = ''
        for player in self.__players:
            team_string += str(player) + ' '
        team_string = team_string[:-1]
        return f"Name {self.name}, Score team: {self.score_team()}, Players: {team_string}"

    def __repr__(self):
        """Representation of the team when printed"""
        return str(self)
