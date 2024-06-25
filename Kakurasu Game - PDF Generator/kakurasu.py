import random


class KakurasuPuzzle:
    def __init__(self, size):
        self.size = size
        self.ans_board = []
        self.qus_grid = []
        self.make_grid()
        self.make_qus()

    def get_qus(self):
        return self.qus_grid

    def get_ans(self):
        return self.ans_board

    def check_board(self):
        length = len(self.ans_board)
        for row in self.ans_board:
            if "B" not in row:
                return False

        for i in range(length):
            this_column = []
            for j in range(length):
                this_column.append(self.ans_board[j][i])

            if "B" not in this_column:
                return False

        return True

    def make_grid(self):
        self.ans_board = [[0] * self.size for i in range(self.size)]
        for row in range(self.size):
            for column in range(self.size):
                choice = random.choice(["B", 0, "B", 0, 0, "B", 0, 0])
                self.ans_board[row][column] = choice

        if self.check_board():
            pass
        else:
            return self.make_grid()

    @staticmethod
    def counter(a_list):
        count = 0
        length = len(a_list)
        for i in range(length):
            if a_list[i] == "B":
                count += i + 1
        return count

    def make_qus(self):
        length = self.size + 2
        self.qus_grid = [[0] * length for j in range(length)]

        for row in range(length):
            for col in range(length):
                if row == 0:
                    if col != 0 and col != length - 1:
                        self.qus_grid[row][col] = col
                if col == 0:
                    if row != 0 and row != length - 1:
                        self.qus_grid[row][col] = row

            for row in range(length - 2):
                count_row = self.counter(self.ans_board[row])
                self.qus_grid[row + 1][-1] = count_row

                this_column = []
                for column in range(length - 2):
                    this_column.append(self.ans_board[column][row])

                count_col = self.counter(this_column)
                self.qus_grid[-1][row + 1] = count_col


def gimme_kakurasu(ans_board_size):
    my_game = KakurasuPuzzle(ans_board_size)
    qus = my_game.get_qus()
    ans = my_game.get_ans()

    return qus, ans


if __name__ == '__main__':
    my_game_ = KakurasuPuzzle(12)
    qus_ = my_game_.get_qus()
    ans_ = my_game_.get_ans()

    for i in qus_:
        print(i)

    print()
    print()
    input("wanna see answer?? ")
    for j in ans_:
        print(j)
