import random
from copy import deepcopy


class NumberSearch:
    def __init__(self, size, each_num_size, positions):
        self.size = size
        self.ans_grid = [["_"] * self.size for _ in range(self.size)]
        self.positions = positions
        self.num_size = each_num_size
        self.ans = []
        self.total_nums = 20
        self.make_board()
        self.qus_grid = deepcopy(self.ans_grid)
        self.make_qus_grid()

    def get_ans_puzzle(self):
        return self.ans_grid

    def get_qus_puzzle(self):
        return self.qus_grid

    def get_ans(self):
        return self.ans

    def make_qus_grid(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.qus_grid[row][col] == "_":
                    self.qus_grid[row][col] = str(random.randint(0, 9))

    def check_possible(self, num, x_start, y_start, step_x, step_y):
        for num_index in range(self.num_size):
            next_x_pos = x_start + (num_index * step_x)
            next_y_pos = y_start + (num_index * step_y)

            if next_x_pos >= self.size or next_y_pos >= self.size:
                return False

            if next_x_pos < 0 or next_y_pos < 0:
                return False

            if self.ans_grid[next_x_pos][next_y_pos] != "_":
                if self.ans_grid[next_x_pos][next_y_pos] == num[num_index]:
                    pass
                else:
                    return False
        return True

    def place(self, num, x_start, y_start, step_x, step_y):
        for num_index in range(self.num_size):
            next_x_pos = x_start + (num_index * step_x)
            next_y_pos = y_start + (num_index * step_y)

            self.ans_grid[next_x_pos][next_y_pos] = num[num_index]

    def make_board(self):
        while self.total_nums != 0:
            number = self.get_num()
            step_x, step_y = self.get_orientation()
            start_x, start_y = self.get_start_pos()
            if self.check_possible(number, start_x, start_y, step_x, step_y):
                self.place(number, start_x, start_y, step_x, step_y)
                self.ans.append(number)
                self.total_nums -= 1

    def get_orientation(self):
        ori = random.choice(self.positions)
        step_x = 0
        step_y = 0

        if ori == "left_to_right":
            step_x = 0
            step_y = 1

        elif ori == "right_to_left":
            step_x = 0
            step_y = -1

        elif ori == "up_to_down":
            step_x = 1
            step_y = 0

        elif ori == "down_to_up":
            step_x = -1
            step_y = 0

        elif ori == "diagonal_down_right":
            step_x = 1
            step_y = 1

        elif ori == "diagonal_down_left":
            step_x = 1
            step_y = -1

        elif ori == "diagonal_up_right":
            step_x = -1
            step_y = 1

        elif ori == "diagonal_up_left":
            step_x = -1
            step_y = -1

        return step_x, step_y

    def get_start_pos(self):
        start_x_pos = random.randrange(0, self.size)
        start_y_pos = random.randrange(0, self.size)
        return start_x_pos, start_y_pos

    def get_num(self):
        first_num = int("1" + ("0" * (self.num_size - 1)))
        last_num = int("1" + ("0" * self.num_size))
        return str(random.randint(first_num, last_num))


def make_number_search(number_size, all_orientation):
    num_search = NumberSearch(20, number_size, all_orientation)
    ans_grid = num_search.get_ans_puzzle()
    qus_grid = num_search.get_qus_puzzle()
    ans_list = num_search.get_ans()

    return qus_grid, ans_grid, ans_list


if __name__ == '__main__':
    all_pos = ['left_to_right', 'up_to_down']
    # 'left_to_right', 'right_to_left', 'up_to_down', 'down_to_up',
    # 'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left'

    a_g, q_g, ans = make_number_search(10, all_pos)

    for i in q_g:
        print(i)

    print()
    print(ans)
    print()
    print()
    print()
    input("answers?? ")
    print()
    for i in a_g:
        print(i)


