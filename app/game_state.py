import enum
from typing import List
from typing import Tuple

""" Enum defining current game state
        BEFORE_START -- before the game started
        START -- game in progress
        FINISHED -- game finished """
class State(enum.Enum):
    BEFORE_START = 0
    START = 1
    FINISHED = 2

""" Defines single game move """
class Move:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

""" Class containing current game state
        Is used to communicate between GUI and game engine """
class GameState:


    def __init__(self):
        self.state = State.BEFORE_START
        self.moves = []
        self.board_state = []
        self.valid_moves = []

    """ Set game state to BEFORE_START """
    def in_menu(self):
        self.state = State.BEFORE_START

    """ Set game state to FINISHED """
    def finished(self):
        self.state = State.FINISHED

    """ Set game state to START """
    def started(self):
        self.state = State.START

    """ Add a new move.
            Move is only added if the game already started.

        Arguments:
            move -- tuple of size 2 with x,y coordinates of the next move

        Return value:
            True -- if the addition was successful
            False -- if the addition was a failure
    """
    def add_move(self, move: Tuple[int]) -> bool:
        if self.state == State.START:
            self.moves.append(Move(move[0], move[1]))
            return True
        return False

    def get_moves(self) -> List[Move]:
        return self.moves

    """ Clear the list of moves """
    def clear_moves(self):
        self.moves.clear()

    def set_board_state(self, state: List[List[int]]):
        self.board_state = state

    def get_board_state(self) -> List[List[int]]:
        return self.board_state

    def set_valid_moves(self, valid_moves: List[List[int]]):
        self.valid_moves = valid_moves

    def get_valid_moves(self) -> List[List[int]]:
        return self.valid_moves

