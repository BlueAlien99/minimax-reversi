from reversi import Reversi

if __name__ == "__main__":
    reversi = Reversi()
    reversi.print_valid_moves()
    print(reversi.num_of_valid_moves)
    reversi.make_a_move(3, 2)
    reversi.print_valid_moves()
    print(reversi.num_of_valid_moves)
    reversi.make_a_move(2, 2)
    reversi.print_valid_moves()
    print(reversi.num_of_valid_moves)
