from numpy import array

def possible_all_pos():
    possible_all_position = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8],
                             [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8],
                             [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8],
                             [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8],
                             [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8],
                             [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8],
                             [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8],
                             [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8],
                             [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8]]

    return possible_all_position


def all_box():
    box1 = [[0, 0], [0, 1], [0, 2],
            [1, 0], [1, 1], [1, 2],
            [2, 0], [2, 1], [2, 2]]

    box2 = [[0, 3], [0, 4], [0, 5],
            [1, 3], [1, 4], [1, 5],
            [2, 3], [2, 4], [2, 5]]

    box3 = [[0, 6], [0, 7], [0, 8],
            [1, 6], [1, 7], [1, 8],
            [2, 6], [2, 7], [2, 8]]

    box4 = [[3, 0], [3, 1], [3, 2],
            [4, 0], [4, 1], [4, 2],
            [5, 0], [5, 1], [5, 2]]

    box5 = [[3, 3], [3, 4], [3, 5],
            [4, 3], [4, 4], [4, 5],
            [5, 3], [5, 4], [5, 5]]

    box5_2 = [[3, 3], [3, 4], [3, 5],
              [4, 3], [4, 4], [4, 5],
              [5, 3], [5, 4], [5, 5]]

    box6 = [[3, 6], [3, 7], [3, 8],
            [4, 6], [4, 7], [4, 8],
            [5, 6], [5, 7], [5, 8]]

    box7 = [[6, 0], [6, 1], [6, 2],
            [7, 0], [7, 1], [7, 2],
            [8, 0], [8, 1], [8, 2]]

    box8 = [[6, 3], [6, 4], [6, 5],
            [7, 3], [7, 4], [7, 5],
            [8, 3], [8, 4], [8, 5]]

    box9 = [[6, 6], [6, 7], [6, 8],
            [7, 6], [7, 7], [7, 8],
            [8, 6], [8, 7], [8, 8]]

    return [box1, box2, box3, box4, box5, box5_2, box6, box7, box8, box9]


def grid_to_one_line(board):
    one_line_grid = []
    for row_ in range(9):
        for column_ in range(9):
            one_line_grid.append(str(board[row_][column_]))

    return "".join(one_line_grid)


def one_line_to_grid(string):
    grid = []
    number = 0
    this_row = []
    for num in string:
        this_row.append(int(num))
        number += 1
        if number == 9:
            number = 0
            grid.append(this_row)
            this_row = []

    return grid


def array_to_grid(the_array):
    grid = []
    for i in the_array:
        this_row = []
        for j in i:
            this_row.append(j)
        grid.append(this_row)

    return grid


def grid_reverse(qus_g, ans_g):
    new_qus_grid = [[0 for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for column in range(9):
            if qus_g[row][column] == 0:
                new_qus_grid[row][column] = ans_g[row][column]
            else:
                new_qus_grid[row][column] = 0

    return new_qus_grid


if __name__ == "__main__":
    example = array([[6, 2, 1, 8, 5, 9, 7, 3, 4],
                     [7, 3, 9, 2, 6, 4, 1, 5, 8],
                     [5, 4, 8, 3, 7, 1, 6, 2, 9],
                     [3, 8, 6, 1, 4, 2, 9, 7, 5],
                     [1, 7, 5, 9, 8, 6, 3, 4, 2],
                     [2, 9, 4, 7, 3, 5, 8, 1, 6],
                     [4, 1, 2, 6, 9, 7, 5, 8, 3],
                     [9, 5, 3, 4, 1, 8, 2, 6, 7],
                     [8, 6, 7, 5, 2, 3, 4, 9, 1]])

    print(array_to_grid(example))

