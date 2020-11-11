import time
import matplotlib.pyplot as plt

from random import randrange

from reversi import Reversi
import ai
import ai2

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
    noprunetimes = []
    prunetimes = []
    player = 2
    comp = 6
    while not rev.is_finished:
        # input('next move')
        ttt = time.process_time()
        if rev.current_player == 1:
            # move = ai.get_optimal_move(rev, player)
            # moveprune = ai2.get_optimal_move(rev, player)
            moveprune = rev.valid_moves_list[randrange(len(rev.valid_moves_list))]
        else:
            # t = time.process_time()
            # move = ai.get_optimal_move(rev, comp)
            # noprunetimes.append(time.process_time() - t)
            t = time.process_time()
            moveprune = ai2.get_optimal_move(rev, comp)
            prunetimes.append(time.process_time() - t)
        print(time.process_time() - ttt)
        if moveprune == (-1, -1):
            print("invalid")
            break
        # assert move == moveprune, f'{move}, {moveprune}'
        assert rev.make_a_move(moveprune[0], moveprune[1])
        pl1score.append(rev.player1_points)
        pl2score.append(rev.player2_points)
        rev.print_board()

    print(rev.player1_points)
    print(rev.player2_points)

    plt.plot(pl1score, color="black")
    plt.plot(pl2score, color='red')
    plt.show()

    # plt.plot(noprunetimes, color="blue")
    # plt.plot(prunetimes, color='red')
    # plt.show()
