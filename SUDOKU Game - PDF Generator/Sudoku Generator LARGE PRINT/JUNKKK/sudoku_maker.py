import random

import level_sudoku
import sudoku_making
import popper
import new_sudo


def random_popper(visible_total_num):
    pop_pos = []
    possible_positions = popper.possible_all_pos()

    for i in range(81 - visible_total_num):
        pop_num = random.choice(possible_positions)
        while pop_num in pop_pos:
            pop_num = random.choice(possible_positions)

        pop_pos.append(pop_num)

    return pop_pos


def specific_popper(visible_list, grid):
    qus_grid = grid

    for row in range(9):
        for column in range(9):
            if qus_grid[row][column] not in visible_list:
                qus_grid[row][column] = 0

    return qus_grid


def make_sudoku():
    grid = sudoku_making.makeBoard()

    ans_grid = [[0 for _ in range(9)] for _ in range(9)]
    qus_grid = [[0 for _ in range(9)] for _ in range(9)]

    # Making Ans Grid
    for row in range(9):
        for column in range(9):
            ans_grid[row][column] = grid[row][column][0]
            qus_grid[row][column] = grid[row][column][0]

    # Making Question Grid
    set_qus = new_sudo.SudokuGenerator(qus_grid)
    set_qus.remove_numbers_from_grid()

    second_qus = new_sudo.SudokuGenerator(set_qus.grid)
    second_qus.remove_numbers_from_grid()

    qus_grid = second_qus.grid

    print(popper.one_line(qus_grid))
    return qus_grid, ans_grid


if __name__ == "__main__":
    qus, ans = make_sudoku(30)
    print(ans)


