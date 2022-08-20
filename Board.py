from Collection import Collection
from Exceptions import InvalidNumberException, EmptyBoardException, FullBoardException


class Board(Collection):

    def __init__(self, max_capacity):
        """
        Constructor
        :param max_capacity: The max dominoes capacity on board
        """
        super().__init__([])
        if max_capacity < 1 or max_capacity > 28:
            raise InvalidNumberException("Max capacity only between 1-28")
        self.max_capacity = max_capacity

    def in_left(self):
        """Checks the most left value on board"""
        if self.array == []:
            raise EmptyBoardException("No Dominoes, Board is empty")
        return self.array[0].get_left()

    def in_right(self):
        """Checks the most right value on board"""
        if self.array == []:
            raise EmptyBoardException("No Dominoes, Board is empty")
        return self.array[len(self.array) - 1].get_right()

    def add(self, domino, add_to_right=True):
        """
        Adds domino to board, placing according to add_to_right value
        :param domino: the domino added
        :param add_to_right: if True add to the right hand of the board, add to left hand otherwise
        :return: True if added, False otherwise
        """
        if len(self.array) == self.max_capacity:
            raise FullBoardException("Board is full, no place to add dominoes")
        if not self.array:
            self.array.append(domino)
            return True
        elif add_to_right:
            if not self.add_right(domino):
                return False
            return True
        else:
            if not self.add_left(domino):
                return False
            return True

    def add_right(self, domino):
        """Add to right in board, trys regular and if not flips the domino"""
        if self.in_right() == domino.get_left():
            self.array.append(domino)
            return True
        else:
            domino = domino.flip()
            if self.in_right() == domino.get_left():
                self.array.append(domino)
                return True
        return False

    def add_left(self, domino):
        """Add to false in board, trys regular and if not flips the domino"""
        if self.in_left() == domino.get_right():
            self.array.insert(0, domino)
            return True
        else:
            domino = domino.flip()
            if self.in_left() == domino.get_right():
                self.array.insert(0, domino)
                return True
        return False

    def __getitem__(self, item):
        """Returns the item in the item index"""
        return self.array[item]

    def __contains__(self, item):
        """Checks if item is in the board"""
        return item in self.array

    def __eq__(self, other):
        """Equalizing boards, according to length, max capacity,
         and each domino and it's place(right side of domino equal and left side of domino equal)"""
        if len(self) == len(other):
            if self.max_capacity == other.max_capacity:
                for i in range(len(self.array)):
                    if self.array[i-1].get_right == other.array[i-1].get_right:
                        if self.array[i-1].get_left == other.array[i-1].get_left:
                            continue
                        else:
                            return False
                    else:
                        return False
                return True
        return False

    def __ne__(self, other):
        """Checks if boards are not equal"""
        if not self == other:
            return True
        return False
