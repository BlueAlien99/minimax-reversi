from app.gui.main import GUI
from app.reversi import Reversi
from app.game_state import GameState, Player, State


if __name__ == "__main__":
    game_state = GameState()
    gui = GUI(game_state)
    reversi = Reversi()

    while True:
        gui.update()
        if (game_state.get_state() == State.RESTARTING):
            reversi.reset()
            game_state.start()
        for move in game_state.get_moves():
            if reversi.make_a_move(move.row, move.col):
                break
        game_state.clear_moves()
        game_state.set_turn(Player(reversi.current_player))
        game_state.set_board_state(reversi.board)
        game_state.set_valid_moves(reversi.valid_moves)
        game_state.set_points(Player.Player1, reversi.player1_points)
        game_state.set_points(Player.Player2, reversi.player2_points)
        gui.draw()
