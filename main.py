import time

from reversi import Reversi
import ai

if __name__ == "__main__":
    print("Somebody once told me")
    print("The world is gonna roll me")
    print("I ain't the sharpest tool in the shed")

    # gods = time.process_time()
    #
    # xxx = 0
    # to = input("how long?")
    # for x in range(int(to)):
    #     xxx += x
    #
    # print(time.process_time() - gods)

    rev = Reversi()
    rev.print_board()
    i = 0
    while not rev.is_finished:
        input('next move')
        t = time.process_time()
        move = ai.get_optimal_move(rev, 6)
        print(time.process_time() - t)
        if move == (-1, -1):
            print("invalid")
            break
        assert rev.make_a_move(move[0], move[1])
        rev.print_board()



