from app.gui.main import GUI
from app.reversi import Reversi
from app.game_state import GameState, Player, State, Property
from app import ai
import sys
from time import sleep


class App:
    def __init__(self):
        self.game_state = GameState()
        self.gui = GUI(self.game_state)
        self.reversi = Reversi()

    def run(self):
        while True:
            self.gui.update()
            if self.game_state.get_state() == State.RESTARTING:
                self.reversi.reset()
                self.game_state.start()
            self.__make_move()
            self.__update_game_state()
            self.gui.draw()

    def __make_move(self):
        current_player = self.game_state.get_current_player()
        is_human = self.game_state.get_player_property(current_player, Property.IS_HUMAN)
        if is_human:
            for move in self.game_state.get_moves():
                if self.reversi.make_a_move(move.row, move.col):
                    break
            self.game_state.clear_moves()
        else:
            sleep(1)
            depth = self.game_state.get_player_property(current_player, Property.DEPTH)
            move = ai.get_optimal_move(self.reversi, depth)
            self.reversi.make_a_move(move[0], move[1])

    def __update_game_state(self):
        self.game_state.set_current_player(Player(self.reversi.current_player))
        self.game_state.set_board_state(self.reversi.board)
        self.game_state.set_valid_moves(self.reversi.valid_moves)
        self.game_state.set_points(Player.Player1, self.reversi.player1_points)
        self.game_state.set_points(Player.Player2, self.reversi.player2_points)


if __name__ == "__main__":
    app = App()
    app.run()
