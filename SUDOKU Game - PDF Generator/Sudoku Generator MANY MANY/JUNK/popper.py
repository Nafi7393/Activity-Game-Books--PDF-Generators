import random


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

    return box1, box2, box3, box4, box5, box5_2, box6, box7, box8, box9


def get_box():
    box1, box2, box3, box4, box5, box5_2, box6, box7, box8, box9 = all_box()
    all_boxes = [box1, box2, box3, box4, box5, box5_2, box6, box7, box8, box9]

    return all_boxes


def one_line(board):
    one_line_grid = []
    for row_ in range(9):
        for column_ in range(9):
            one_line_grid.append(str(board[row_][column_]))

    return "".join(one_line_grid)


def grid_reverse(qus_g, ans_g):
    new_qus_grid = [[0 for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for column in range(9):
            if qus_g[row][column] == 0:
                new_qus_grid[row][column] = ans_g[row][column]
            else:
                new_qus_grid[row][column] = 0

    return new_qus_grid


def must_stay(grid):
    need_pos = []
    final_pos = []
    common = []
    return_lst = []

    def check_row_two_digi():
        for i in range(8):
            for row in range(8 - i):
                container = []
                position = []
                two_list = []
                for column in range(9):
                    num1 = grid[row][column]
                    num2 = grid[row + 1 + i][column]

                    if num1 == 0 or num2 == 0:
                        two_list = []
                    else:
                        two_list.append(num1)
                        two_list.append(num2)

                        position.append([[row, column], [(row + 1 + i), column]])

                        for item in container:
                            if item[0] in two_list:
                                if item[1] in two_list:
                                    item_index_in_pos = container.index(item)
                                    need_pos.append(position[item_index_in_pos])
                                    need_pos.append([[row, column], [(row + 1 + i), column]])
                        container.append(two_list)
                        two_list = []

    def check_column_two_digi():
        for i in range(8):
            for row in range(8 - i):
                container = []
                position = []
                two_list = []
                for column in range(9):
                    num1 = grid[column][row]
                    num2 = grid[column][row + 1 + i]

                    if num1 == 0 or num2 == 0:
                        two_list = []
                    else:
                        two_list.append(num1)
                        two_list.append(num2)

                        position.append([[column, row], [column, (row + 1 + i)]])

                        for item in container:
                            if item[0] in two_list:
                                if item[1] in two_list:
                                    item_index_in_pos = container.index(item)
                                    need_pos.append(position[item_index_in_pos])
                                    need_pos.append([[column, row], [column, (row + 1 + i)]])

                        container.append(two_list)
                        two_list = []

    def check_row_three_digi():
        for i in range(7):
            container = []
            for row in range(7 - i):
                for column in range(9):
                    num1 = grid[row + i][column]
                    num2 = grid[row + 1 + i][column]
                    num3 = grid[row + 2 + i][column]

                    if num1 == 0 or num2 == 0 or num3 == 0:
                        pass
                    else:
                        pos = [[row + i, column], [row + 1 + i, column], [row + 2 + i, column]]
                        num_lst = [num1, num2, num3]
                        for item in container:
                            if item[0] in num_lst:
                                if item[1] in num_lst:
                                    if item[2] in num_lst:
                                        if pos not in final_pos:
                                            final_pos.append(pos)
                        container.append(num_lst)
                container = []

    def check_column_three_digi():
        for i in range(7):
            container = []
            for row in range(7 - i):
                for column in range(9):
                    num1 = grid[column][row + i]
                    num2 = grid[column][row + 1 + i]
                    num3 = grid[column][row + 2 + i]

                    if num1 == 0 or num2 == 0 or num3 == 0:
                        pass
                    else:
                        pos = [[column, row + i], [column, row + 1 + i], [column, row + 2 + i]]
                        num_lst = [num1, num2, num3]
                        for item in container:
                            if item[0] in num_lst:
                                if item[1] in num_lst:
                                    if item[2] in num_lst:
                                        if pos not in final_pos:
                                            final_pos.append(pos)
                        container.append(num_lst)
                container = []

    check_row_two_digi()
    check_column_two_digi()
    check_row_three_digi()
    check_column_three_digi()

    for items in final_pos:
        for itm in items:
            for need_item in need_pos:
                if itm in need_item:
                    if itm not in common:
                        common.append(itm)
                        return_lst.append(itm)

    for must in need_pos:
        def get_common():
            while True:
                if must[0] not in return_lst:
                    return_lst.append(must[0])
                    break
                elif must[1] not in return_lst:
                    return_lst.append(must[1])
                    break
                break

        def get_all():
            return_lst.append(must[0])
            return_lst.append(must[1])

        get_common()

    return return_lst


if __name__ == "__main__":
    qus_grid = [[0,0,0,6,0,0,8,0,4],
                [0,4,0,1,0,0,0,0,0],
                [9,5,6,4,0,0,0,0,3],
                [0,3,9,0,4,0,0,0,7],
                [4,0,0,0,1,0,0,0,0],
                [6,0,0,0,2,0,1,4,0],
                [7,1,3,0,0,0,0,9,6],
                [5,9,0,0,0,1,7,8,0],
                [2,6,8,0,9,7,0,3,1]]

    ans_grid = [[3,2,1,6,5,9,8,7,4],
                [8,4,7,1,3,2,9,6,5],
                [9,5,6,4,7,8,2,1,3],
                [1,3,9,8,4,5,6,2,7],
                [4,7,2,9,1,6,3,5,8],
                [6,8,5,7,2,3,1,4,9],
                [7,1,3,2,8,4,5,9,6],
                [5,9,4,3,6,1,7,8,2],
                [2,6,8,5,9,7,4,3,1]]

    print(len(must_stay(ans_grid)))
    print(one_line(qus_grid))

























