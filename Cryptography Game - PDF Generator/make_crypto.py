import random


def set_all_lines(word_file_name):
    handel = open(f"{word_file_name}")
    all_line = handel.readlines()
    handel.close()
    line_list = []
    for i in range(len(all_line)):
        line_list.append(all_line[i].strip("\n").upper())

    return line_list


def make_random_strings():
    correct_strings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    random_string = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    random.shuffle(random_string)
    return random_string, correct_strings


def make_crypto(line, random_str, correct_str):
    last_str = []
    line_list = list(line)
    for i in range(len(line_list)):
        if line_list[i] == "A":
            last_str.append(random_str[0])

        if line_list[i] == "B":
            last_str.append(random_str[1])

        if line_list[i] == "C":
            last_str.append(random_str[2])

        if line_list[i] == "D":
            last_str.append(random_str[3])

        if line_list[i] == "E":
            last_str.append(random_str[4])

        if line_list[i] == "F":
            last_str.append(random_str[5])

        if line_list[i] == "G":
            last_str.append(random_str[6])

        if line_list[i] == "H":
            last_str.append(random_str[7])

        if line_list[i] == "I":
            last_str.append(random_str[8])

        if line_list[i] == "J":
            last_str.append(random_str[9])

        if line_list[i] == "K":
            last_str.append(random_str[10])

        if line_list[i] == "L":
            last_str.append(random_str[11])

        if line_list[i] == "M":
            last_str.append(random_str[12])

        if line_list[i] == "N":
            last_str.append(random_str[13])

        if line_list[i] == "O":
            last_str.append(random_str[14])

        if line_list[i] == "P":
            last_str.append(random_str[15])

        if line_list[i] == "Q":
            last_str.append(random_str[16])

        if line_list[i] == "R":
            last_str.append(random_str[17])

        if line_list[i] == "S":
            last_str.append(random_str[18])

        if line_list[i] == "T":
            last_str.append(random_str[19])

        if line_list[i] == "U":
            last_str.append(random_str[20])

        if line_list[i] == "V":
            last_str.append(random_str[21])

        if line_list[i] == "W":
            last_str.append(random_str[22])

        if line_list[i] == "X":
            last_str.append(random_str[23])

        if line_list[i] == "Y":
            last_str.append(random_str[24])

        if line_list[i] == "Z":
            last_str.append(random_str[25])

        for j in range(26):
            if line_list[i] in correct_str:
                pass
            else:
                last_str.append(line_list[i])
                break

    return "".join(last_str)


if __name__ == "__main__":
    original_lines = set_all_lines("lines.txt")
    cryptoo_lines = []
    for total_lines in range(len(original_lines)):
        random_string, correct_string = make_random_strings()
        cryptoo_lines.append(make_crypto(original_lines[total_lines], random_string, correct_string))

    print(cryptoo_lines[0])
    print(original_lines[0])




