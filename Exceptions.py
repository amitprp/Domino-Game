class EmptyBoardException(Exception):
    """ Raised when board is empty"""
    pass


class FullBoardException(Exception):
    """Raise when board is full with dominoes"""
    pass


class NoSuchDominoException(Exception):
    """Raised when there's no such domino the collection"""
    pass


class InvalidNumberException(Exception):
    """Raised when the number is not the range"""
    def __str__(self):
        return f"ERROR {super().__str__()}"
    pass
