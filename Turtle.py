import numpy as np


class Turtle():
    """
    Class Turtle. Contains attributes:
    :param position: Stores turtle's position
    :type position: list

    :param turn: Stores turtle's turn
    :type turn: int
    """

    def __init__(self, position, turn):
        """Constructs a turtle with a given position and a turn."""
        self.position = position if position is not None else [0, 0]
        self.turn = turn if turn is not None else 0

    def __str__(self):
        """Returns basic description of the turtle."""
        return f'the turtle is on {self.position} with {self.turn} turn'

    def position_now(self):
        """Getting turtle's position."""
        return np.array(self.position)

    def turning_now(self):
        """Getting turtle's turn."""
        return self.turn
