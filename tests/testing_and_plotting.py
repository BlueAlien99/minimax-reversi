"""
    Usage: python3 program_name [player_1_depth] [player2_depth]
"""

import time
import matplotlib.pyplot as plt

from random import randrange

from app.reversi import Reversi
from app import ai2
from app import ai

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 program_name [player_1_depth] [player2_depth]")
        sys.exit()

    # gods = time.process_time()
    #
    # xxx = 0
    # to = input("how long?")
    # for x in range(int(to)):
    #     xxx += x
    #
    # print(time.process_time() - gods)

    game = Reversi()
    game.print_board()
    print("")
    i = 0
    pl1score = []
    pl2score = []
    noprunetimes = []
    prunetimes = []
    p1_depth = int(sys.argv[1])
    p2_depth = int(sys.argv[2])

    while not game.is_finished:
        # input('next move')
        ttt = time.process_time()
        if game.current_player == 1:
            # move = ai.get_optimal_move(game, player)
            moveprune = ai.get_optimal_move(game, p1_depth)
            # moveprune = game.valid_moves_list[randrange(len(game.valid_moves_list))]
        else:
            # t = time.process_time()
            # move = ai.get_optimal_move(game, comp)
            # noprunetimes.append(time.process_time() - t)
            t = time.process_time()
            moveprune = ai.get_optimal_move(game, p2_depth)
            prunetimes.append(time.process_time() - t)
        if moveprune == (-1, -1):
            print("invalid move")
            break
        # assert move == moveprune, f'{move}, {moveprune}'
        print("Player: " + str(game.current_player))
        print("Time took: " + str(time.process_time() - ttt))
        assert game.make_a_move(moveprune[0], moveprune[1])
        pl1score.append(game.player1_points)
        pl2score.append(game.player2_points)
        print("P1 score: " + str(game.player1_points) + "\tP2 score: " + str(game.player2_points))
        game.print_board()
        print("")

    print(game.player1_points)
    print(game.player2_points)

    # Display plot showing points over time
    plt.ylabel('points')
    plt.xlabel('number of moves')
    plt.plot(pl1score, color="black")
    plt.plot(pl2score, color='red')
    plt.legend(['player1', 'player2'])
    if not os.path.exists('tests/plots'):
        os.mkdir('tests/plots')
    plt.savefig("tests/plots/" + str(p1_depth) + str(p2_depth) + ".png")
    plt.show()

    # plt.plot(noprunetimes, color="blue")
    # plt.plot(prunetimes, color='red')
    # plt.show()
