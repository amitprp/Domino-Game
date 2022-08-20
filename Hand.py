from Collection import Collection
from Exceptions import NoSuchDominoException


class Hand(Collection):
    def __init__(self, dominoes):
        """Constructor using Collection, sending dominoes for array"""
        super().__init__(dominoes)

    def add(self, domino, index=None):
        """Adding a domino to hand in the index input"""
        # Adding To the end of the hand
        if index is None:
            self.array.append(domino)
        else:
            self.array.insert(index, domino)

    def remove_domino(self, domino):
        """Removing domino from the hand"""
        for i in range(len(self.array)):
            if self[i] == domino:
                self.array.pop(i)
                return i
        raise NoSuchDominoException("No such domino in the hand")

    def __getitem__(self, i):
        """Returns the item in the hand in the i place"""
        return self.array[i]

    def __eq__(self, other):
        """Equalizing hands by equal dominoes in the same place"""
        for i in range(len(self)):
            if not self[i-1] == other[i-1]:
                return False
        return True

    def __ne__(self, other):
        """Checking if hands are not equal"""
        if self == other:
            return False
        return True
