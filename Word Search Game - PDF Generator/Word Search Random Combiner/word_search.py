import random


def make_grid(grid_size):
    grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]
    return grid


def set_all_words(word_file_name):
    handel = open(f"{word_file_name}")
    worrds = handel.readlines()
    new_wrd = []
    for wrd in worrds:
        wrd = wrd.upper().replace("\n", "")
        new_wrd.append(wrd)
    handel.close()
    return new_wrd


words = set_all_words("_word.txt")
used_words = []


def get_this_many_word_per_page(this_many, same_word="yes"):
    global used_words
    global words
    random.shuffle(words)
    per_page_word = []
    total_word_need = this_many
    if same_word == "no":
        while total_word_need != 0:
            the_word = random.choice(words)
            if the_word in used_words:
                continue
            else:
                used_words.append(the_word)
                per_page_word.append(the_word)
                total_word_need -= 1
    else:
        while total_word_need != 0:
            if len(words) < 20:
                for wrdss in used_words:
                    words.append(wrdss)
                used_words = []
            the_word = random.choice(words)

            if the_word not in per_page_word:
                per_page_word.append(the_word)
                used_words.append(the_word)
                total_word_need -= 1
                words.remove(the_word)

    return per_page_word


def is_it_possiable(word, length, start_x, start_y, x_move, y_move, the_grid, grid_size):
    for word_index in range(length):
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


def make_qus_grid(ans_grid, grid_size):
    for x in range(grid_size):
        all_strings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for y in range(grid_size):
            if ans_grid[x][y] == '_':
                ans_grid[x][y] = random.choice(all_strings)

    return ans_grid


all_orientations = ['left_to_right', 'right_to_left', 'up_to_down', 'down_to_up',
                    'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left']
# 'left_to_right', 'right_to_left', 'up_to_down', 'down_to_up', 'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left'


def make_word_search(grid_size, per_page_this_many_words=10, orientations=all_orientations, same_word_repate="no"):
    same_word_repate = same_word_repate.lower()

    grid = make_grid(grid_size)
    per_page_word = get_this_many_word_per_page(per_page_this_many_words, same_word_repate)

    for word in per_page_word:
        word = word.replace(" ", "")
        word_length = len(word)
        placed = False

        while not placed:
            start_x_pos = random.randrange(0, grid_size)
            start_y_pos = random.randrange(0, grid_size)
            orientation = random.choice(orientations)
            if orientation == "left_to_right":
                step_x = 0
                step_y = 1

            if orientation == "right_to_left":
                step_x = 0
                step_y = -1

            if orientation == "up_to_down":
                step_x = 1
                step_y = 0

            if orientation == "down_to_up":
                step_x = -1
                step_y = 0

            if orientation == "diagonal_down_right":
                step_x = 1
                step_y = 1

            if orientation == "diagonal_down_left":
                step_x = 1
                step_y = -1

            if orientation == "diagonal_up_right":
                step_x = -1
                step_y = 1

            if orientation == "diagonal_up_left":
                step_x = -1
                step_y = -1

            if is_it_possiable(word, word_length, start_x_pos, start_y_pos, step_x, step_y, grid, grid_size):
                for place_word in range(word_length):
                    place_x_pos = start_x_pos + (place_word * step_x)
                    place_y_pos = start_y_pos + (place_word * step_y)

                    grid[place_x_pos][place_y_pos] = word[place_word]

                    if place_word == word_length - 1:
                        placed = True

    return grid, per_page_word


if __name__ == "__main__":
    grid, answers = make_word_search(20, 20)

    for row in range(len(grid)):
        for column in range(len(grid)):
            print(f"\t{grid[row][column]}", end="")
        print("")

    make_qus_grid(grid, 20)

    for row in range(len(grid)):
        for column in range(len(grid)):
            print(f"\t{grid[row][column]}", end="")
        print("")

    print(answers)


