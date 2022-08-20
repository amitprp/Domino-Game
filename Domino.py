import copy
from Exceptions import InvalidNumberException


class Domino:
    def __init__(self, left, right):
        """
        Constructor
        :param left: Left side of the domino
        :param right: Right side of the domino
        """
        if 0 > left or left > 6 or 0 > right or right > 6:
            raise InvalidNumberException("Can only input integers in between 0-6 including, to the sides of the domino.")
        self.__left_side = left
        self.__right_side = right

    def get_left(self):
        """Returns left side of domino"""
        return copy.deepcopy(self.__left_side)

    def get_right(self):
        """Returns right side of domino"""
        return copy.deepcopy(self.__right_side)

    def __str__(self):
        """string of the domino as a list with '|' between to indicate sides"""
        return f"[{self.get_left()}|{self.get_right()}]"

    def __eq__(self, other):
        """Equalizing dominoes, if the 2 dominoes has same numbers, no matter the sides"""
        if isinstance(other, Domino):
            if other.get_right() == self.get_right():
                if other.get_left() == self.get_left():
                    return True
                return False
            elif other.get_left() == self.get_right():
                if other.get_right() == self.get_left():
                    return True
        return False

    def __gt__(self, other):
        """If a value of a whole domino(sum of both sides) is bigger than the other"""
        score_self = self.get_right() + self.get_left()
        score_other = other.get_right() + other.get_left()
        if score_self > score_other:
            return True
        return False

    def __contains__(self, key):
        """If a numbers is in a domino"""
        if key == self.get_right() or key == self.get_left():
            return True
        return False

    def flip(self):
        """Flipping sides of dominoes"""
        return Domino(self.get_right(), self.get_left())

    def __repr__(self):
        """Representation of domino when printing"""
        return str(self)




