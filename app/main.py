from gui.main import GUI
from reversi import Reversi
from game_state import GameState

game_state = GameState()
gui = GUI(game_state)
reversi = Reversi()

while True:
    game_state.set_board_state(reversi.board)
    game_state.set_valid_moves(reversi.valid_moves)
    moves = gui.update()
    for move in game_state.get_moves():
        if reversi.make_a_move(move.row, move.col):
            break
