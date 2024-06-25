import copy
import random
import os


def get_all_words():
    def get_question_files(folder_name="_all_words"):
        filenames = next(os.walk(f"{folder_name}"), (None, None, []))[2]  # [] if no file
        return filenames

    def format_files_name_for_key(files):
        lst = []
        for i in files:
            i = i.replace("_", "")
            lst.append(i)
        return lst

    def set_all_words(all_files):
        final_dict = {}
        for file in all_files:
            this_file = file.replace("_", "")
            final_dict[this_file] = []
            with open(f"_all_words/{file}", "r") as reading:
                words = reading.readlines()
                for wrd in words:
                    wrd = wrd.upper().replace("\n", "")
                    final_dict[this_file].append(wrd)
        return final_dict
    files_names = get_question_files()
    return set_all_words(files_names), format_files_name_for_key(files_names)


def make_grid(grid_size):
    grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]
    return grid


def is_it_possible(word, word_length, start_x, start_y, x_move, y_move, the_grid):
    grid_size = len(the_grid)
    for word_index in range(word_length):
        next_x_pos = start_x + (word_index * x_move)
        next_y_pos = start_y + (word_index * y_move)

        if next_x_pos >= grid_size or next_y_pos >= grid_size:
            return False

        if next_x_pos < 0 or next_y_pos < 0:
            return False

        if the_grid[next_x_pos][next_y_pos] != "_":
            if the_grid[next_x_pos][next_y_pos] == word[word_index]:
                pass
            else:
                return False
    return True


def get_orin(orientations):
    ori = random.choice(orientations)
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


all_word_dict, keys = get_all_words()
key_pos = 0
keys_length = len(keys)


def get_words_for_puzzle():
    global all_word_dict
    global keys
    global key_pos

    this_puzzle = {}
    if key_pos >= keys_length:
        key_pos = 0
        all_word_dict, keys = get_all_words()

    key = keys[key_pos]
    this_puzzle[key] = []
    if len(all_word_dict[key]) >= 12:
        random.shuffle(all_word_dict[key])
        for _ in range(20):
            try:
                this_puzzle[key].append(all_word_dict[key].pop())
            except IndexError:
                pass

    if len(this_puzzle[key]) != 0:
        return this_puzzle
    else:
        key_pos += 1
        return get_words_for_puzzle()


def make_word_search(grid_size, orient):
    def make_qus_grid(board):
        qus = copy.deepcopy(board)
        for x in range(grid_size):
            all_strings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for y in range(grid_size):
                if qus[x][y] == '_':
                    qus[x][y] = random.choice(all_strings)
        return qus

    ans_grid = make_grid(grid_size)
    ans = get_words_for_puzzle()
    for word in ans.values():
        for this_word in word:
            this_word = this_word.replace(" ", "")
            word_length = len(this_word)
            placed = False

            while not placed:
                start_x_pos = random.randrange(0, grid_size)
                start_y_pos = random.randrange(0, grid_size)
                step_x, step_y = get_orin(orient)
                if is_it_possible(this_word, word_length, start_x_pos, start_y_pos, step_x, step_y, ans_grid):
                    for place_word in range(word_length):
                        place_x_pos = start_x_pos + (place_word * step_x)
                        place_y_pos = start_y_pos + (place_word * step_y)

                        ans_grid[place_x_pos][place_y_pos] = this_word[place_word]

                        if place_word == word_length - 1:
                            placed = True
    return make_qus_grid(ans_grid), ans_grid, ans


if __name__ == '__main__':
    all_orientations = ['left_to_right', 'right_to_left', 'up_to_down', 'down_to_up',
                        'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left']

    q_grid, a_grid, answers = make_word_search(20, all_orientations)

    for row in range(len(q_grid)):
        for column in range(len(q_grid)):
            print(f"\t{q_grid[row][column]}", end="")
        print("")

    print(answers)

    for row in range(len(a_grid)):
        for column in range(len(a_grid)):
            print(f"\t{a_grid[row][column]}", end="")
        print("")

