import requests
from bs4 import BeautifulSoup
import random
import copy
import time

import functions


class MakeSudoku:
    def __init__(self, minimum_visible_num=17):
        """
        minimum_visible_num must have minimum value of 17 and cannot be higher than 81
        """
        self.ans_collector = []
        self.base = 3
        self.side = self.base * self.base
        self.minimum_visible = minimum_visible_num

        self.grid = self.make_valid_board()
        self.ans_grid = copy.deepcopy(self.grid)

        self.digger(number=0, holes_num=0)

    def get_all_number_and_pos(self):
        num_and_pos = []
        for row in range(9):
            for column in range(9):
                if self.grid[row][column] != 0:
                    num_and_pos.append([self.grid[row][column], [row, column]])

        return num_and_pos

    def make_valid_board(self):
        # pattern for a baseline valid solution
        def pattern(row, column):
            return (self.base * (row % self.base) + row // self.base + column) % self.side

        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(s):
            return random.sample(s, len(s))

        r_base = range(self.base)
        rows = [g * self.base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g * self.base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, self.base * self.base + 1))

        # produce board using randomized baseline pattern
        return [[nums[pattern(row, column)] for column in cols] for row in rows]

    def count(self):
        self.solve()

        if len(self.ans_collector) > 1:
            return False
        if len(self.ans_collector) == 1:
            return True

    def possible_num(self, row, column, number):
        # Is the number appearing in the given row?
        for i in range(0, 9):
            if self.grid[row][i] == number:
                return False

        # Is the number appearing in the given column?
        for i in range(0, 9):
            if self.grid[i][column] == number:
                return False

        # Is the number appearing in the given square?
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y0 + i][x0 + j] == number:
                    return False
        return True

    def solve(self):
        if len(self.ans_collector) > 1:
            return False
        for row in range(0, 9):
            for column in range(0, 9):
                if self.grid[row][column] == 0:
                    for number in range(1, 10):
                        if self.possible_num(row, column, number):
                            self.grid[row][column] = number
                            self.solve()
                            self.grid[row][column] = 0

                    return
        self.ans_collector.append(self.grid)

    def digger(self, number, holes_num):
        if number >= 81 or holes_num >= 81 - self.minimum_visible:
            return

        all_possible_pos = self.get_all_number_and_pos()
        get_one = random.choice(all_possible_pos)
        [row, col] = get_one[1]
        if self.grid[row][col] > 0:
            pz_check = self.grid.copy()
            pz_check[row][col] = 0
            total_solution = self.count()
            if total_solution:
                self.ans_collector = []
                self.grid[row][col] = 0
                holes_num += 1
            else:
                self.grid[row][col] = get_one[0]
                self.ans_collector = []

        self.digger(number=number + 1, holes_num=holes_num)


def make_sudoku(minimum_visible_num=17):
    '''' Minimum_visible_num must have minimum value of 17 and cannot be higher than 81 '''

    new_sudoku = MakeSudoku(minimum_visible_num)
    qus_grid = new_sudoku.grid
    ans_grid = new_sudoku.ans_grid
    print(functions.grid_to_one_line(qus_grid))

    return qus_grid, ans_grid


def make_sudoku_pattern(level=4):
    time.sleep(5)
    html_doc = requests.get(f"https://nine.websudoku.com/?level={level}").content
    soup = BeautifulSoup(html_doc, features="lxml")
    ids = ['f00', 'f01', 'f02', 'f03', 'f04', 'f05', 'f06', 'f07', 'f08', 'f10', 'f11',
           'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f20', 'f21', 'f22', 'f23',
           'f24', 'f25', 'f26', 'f27', 'f28', 'f30', 'f31', 'f32', 'f33', 'f34', 'f35',
           'f36', 'f37', 'f38', 'f40', 'f41', 'f42', 'f43', 'f44', 'f45', 'f46', 'f47',
           'f48', 'f50', 'f51', 'f52', 'f53', 'f54', 'f55', 'f56', 'f57', 'f58', 'f60',
           'f61', 'f62', 'f63', 'f64', 'f65', 'f66', 'f67', 'f68', 'f70', 'f71', 'f72',
           'f73', 'f74', 'f75', 'f76', 'f77', 'f78', 'f80', 'f81', 'f82', 'f83', 'f84',
           'f85', 'f86', 'f87', 'f88']
    data = []
    for cid in ids:
        data.append(soup.find('input', id=cid))
    qus_grid = [[0 for x in range(9)] for x in range(9)]
    for index, cell in enumerate(data):
        try:
            qus_grid[index // 9][index % 9] = int(cell['value'])
        except:
            pass

    ans_line = soup.find('input', id="cheat")["value"]
    ans_grid = functions.one_line_to_grid(ans_line)

    print(functions.grid_to_one_line(qus_grid))
    return qus_grid, ans_grid


if __name__ == "__main__":
    make_sudoku_pattern()


