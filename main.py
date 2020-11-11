import time
import matplotlib.pyplot as plt

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
    pl1score = []
    pl2score = []
    while not rev.is_finished:
        # input('next move')
        t = time.process_time()
        if rev.current_player == 1:
            move = ai.get_optimal_move(rev, 3)
        else:
            move = ai.get_optimal_move(rev, 5)
        print(time.process_time() - t)
        if move == (-1, -1):
            print("invalid")
            break
        assert rev.make_a_move(move[0], move[1])
        pl1score.append(rev.player1_points)
        pl2score.append(rev.player2_points)
        rev.print_board()

    print(rev.player1_points)
    print(rev.player2_points)

    plt.plot(pl1score, color="black")
    plt.plot(pl2score, color='red')
    plt.show()

