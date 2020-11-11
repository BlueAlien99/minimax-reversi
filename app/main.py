from gui.main import GUI
from reversi import Reversi

gui = GUI()
reversi = Reversi()

print(reversi.valid_moves)
while True:
    moves = gui.update(reversi.board, reversi.valid_moves)
    for move in moves:
        if reversi.make_a_move(move[0], move[1]):
            break

