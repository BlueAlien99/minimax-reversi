import copy


class Reversi:
    def __init__(self):
        self.board_size = 8
        self.board = [[0] * self.board_size for x in range(self.board_size)]
        self.init_board()
        self.current_player = 1
        self.valid_moves = self.get_valid_moves()
        self.num_of_valid_moves = self.count_valid_moves()
        self.is_finished = False
        self.player1_points = self.count_points(1)
        self.player2_points = self.count_points(2)

    def init_board(self):
        self.board[3][3] = 2
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = 2

    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=' ')
            print()

    def print_valid_moves(self):
        for row in self.get_valid_moves():
            for col in row:
                if col == -1:
                    print('-', end=' ')
                else:
                    print(col, end=' ')
            print()

    def make_a_move(self, row, col):
        if not self.is_finished and self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.flip_in_dir(row, col, 1, 0)
            self.flip_in_dir(row, col, 1, 1)
            self.flip_in_dir(row, col, 0, 1)
            self.flip_in_dir(row, col, -1, 1)
            self.flip_in_dir(row, col, -1, 0)
            self.flip_in_dir(row, col, -1, -1)
            self.flip_in_dir(row, col, 0, -1)
            self.flip_in_dir(row, col, 1, -1)
            self.player1_points = self.count_points(1)
            self.player2_points = self.count_points(2)
            self.current_player = 2 if self.current_player == 1 else 1
            self.valid_moves = self.get_valid_moves()
            self.num_of_valid_moves = self.count_valid_moves()
            if self.num_of_valid_moves == 0:
                self.current_player = 2 if self.current_player == 1 else 1
                self.valid_moves = self.get_valid_moves()
                self.num_of_valid_moves = self.count_valid_moves()
                if self.num_of_valid_moves == 0:
                    self.is_finished = True
            return True
        return False

    def get_valid_moves(self):
        valid_moves = copy.deepcopy(self.board)
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.is_valid_move(row, col):
                    valid_moves[row][col] = -1
        return valid_moves

    def count_valid_moves(self):
        count = 0
        for row in self.valid_moves:
            for col in row:
                if col == -1:
                    count += 1
        return count

    def is_valid_move(self, row, col):
        if self.board[row][col] == 0:
            if (self.is_valid_in_dir(row, col, 1, 0)
                    or self.is_valid_in_dir(row, col, 1, 1)
                    or self.is_valid_in_dir(row, col, 0, 1)
                    or self.is_valid_in_dir(row, col, -1, 1)
                    or self.is_valid_in_dir(row, col, -1, 0)
                    or self.is_valid_in_dir(row, col, -1, -1)
                    or self.is_valid_in_dir(row, col, 0, -1)
                    or self.is_valid_in_dir(row, col, 1, -1)):
                return True
        return False

    def is_valid_in_dir(self, row, col, row_dir, col_dir):
        opponent = 2 if self.current_player == 1 else 1
        next_row = row + row_dir
        next_col = col + col_dir
        if not self.is_out_of_bounds(next_row, next_col) and self.board[next_row][next_col] == opponent:
            while not self.is_out_of_bounds(next_row, next_col) and self.board[next_row][next_col] != 0:
                if self.board[next_row][next_col] == self.current_player:
                    return True
                next_row += row_dir
                next_col += col_dir
        return False

    def flip_in_dir(self, row, col, row_dir, col_dir):
        opponent = 2 if self.current_player == 1 else 1
        next_row = row + row_dir
        next_col = col + col_dir
        if self.is_valid_in_dir(row, col, row_dir, col_dir):
            while not self.is_out_of_bounds(next_row, next_col) and self.board[next_row][next_col] == opponent:
                self.board[next_row][next_col] = self.current_player
                next_row += row_dir
                next_col += col_dir

    def is_out_of_bounds(self, row, col):
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return True
        return False

    def count_points(self, player):
        count = 0
        for row in self.board:
            for col in row:
                if col == player:
                    count += 1
        return count
