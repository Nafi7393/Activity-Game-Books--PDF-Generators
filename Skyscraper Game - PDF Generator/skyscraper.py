import random
import functions


class Skyscraper:
    def __init__(self):
        self.size = 9
        self.base = 3
        self.grid = self.make_ans_grid()
        self.qus_grid = [[0 for _ in range(self.size + 2)] for _ in range(self.size + 2)]
        self.make_qus_grid()

    def ans_board(self):
        return self.grid

    def qus_board(self):
        return self.qus_grid

    def get_possible_numbers(self):
        return [i for i in range(1, self.size + 1)]

    def get_count(self, this_list):
        count = 0
        set_this = 0
        for i in this_list:
            if set_this < i:
                count += 1
                set_this = i
            if set_this == self.size:
                break
        return count

    def check_possible(self, row, col, num):
        if num in self.grid[row]:
            return False

        for r in range(self.size):
            if self.grid[r][col] == num:
                return False
        return True

    def check_valid_board(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == 0:
                    return False
        return True

    def make_ans_grid(self):
        # pattern for a baseline valid solution
        def pattern(row, column):
            return (self.base * (row % self.base) + row // self.base + column) % self.size

        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(s):
            return random.sample(s, len(s))

        r_base = range(self.base)
        rows = [g * self.base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g * self.base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, self.base * self.base + 1))

        # produce board using randomized baseline pattern
        return [[nums[pattern(row, column)] for column in cols] for row in rows]

    def make_qus_grid(self):
        # This is for checking Rows
        item = 1
        for row in range(self.size):
            this_row = []
            for column in range(self.size):
                this_row.append(self.grid[row][column])

            count = self.get_count(this_row)
            self.qus_grid[item][0] = count

            this_row.reverse()
            count = self.get_count(this_row)
            self.qus_grid[item][-1] = count
            this_row.reverse()
            item += 1

        # This is for checking Columns
        item = 1
        for row in range(self.size):
            this_column = []
            for column in range(self.size):
                this_column.append(self.grid[column][row])

            count = self.get_count(this_column)
            self.qus_grid[0][item] = count

            this_column.reverse()
            count = self.get_count(this_column)
            self.qus_grid[-1][item] = count
            this_column.reverse()
            item += 1


def make_skyscraper():
    while True:
        try:
            sky = Skyscraper()
            break
        except:
            pass

    return sky.ans_board(), sky.qus_board()


if __name__ == '__main__':
    ans, qus = make_skyscraper()

    functions.print_grid(ans)
    functions.print_grid(qus)


