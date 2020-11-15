from app.gui.main import GUI
from app.reversi import Reversi
from app.game_state import GameState, TurnOf, State


if __name__ == "__main__":
    game_state = GameState()
    gui = GUI(game_state)
    reversi = Reversi()

    while True:
        game_state.set_turn(TurnOf(reversi.current_player))
        game_state.set_board_state(reversi.board)
        game_state.set_valid_moves(reversi.valid_moves)
        gui.update()
        if (game_state.get_state() == State.RESTARTING):
            reversi.reset()
            game_state.start()
        for move in game_state.get_moves():
            if reversi.make_a_move(move.row, move.col):
                break
        game_state.clear_moves()
        gui.draw()
