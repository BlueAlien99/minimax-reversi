from app.gui.main import GUI
from app.reversi import Reversi
from app.game_state import GameState


if __name__ == "__main__":
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
