import random


def get_words(file_name, size=0):
    final_word_list = []
    all_word_list = []
    with open(f"{file_name}.txt", "r") as all_words:
        for word in all_words:
            all_word_list.append(word.strip("\n"))
    if size != 0:
        if len(all_word_list) < size:
            raise "Not Enough Words are in the word File"
        else:
            for i in range(size):
                random.shuffle(all_word_list)
                final_word_list.append(all_word_list.pop())
        if len(final_word_list) % 2 != 0:
            final_word_list.pop()
        return final_word_list
    if len(all_word_list) % 2 != 0:
        all_word_list.pop()
    return all_word_list


def get_words_scramble(words):
    all_word_list = []
    for word in words:
        if " " not in word:
            shuffled = ''.join(random.sample(word, len(word)))
            while shuffled == word:
                shuffled = ''.join(random.sample(word, len(word)))
                if len(shuffled) == 1:
                    break
            all_word_list.append(shuffled)
        else:
            this_word = word.split(" ")
            word = get_words_scramble(this_word)
            all_word_list.append(" ".join(word))
    return all_word_list


def word_scramble(file_name, how_many_word=0):
    all_original_word = get_words(file_name, size=how_many_word)
    random.shuffle(all_original_word)
    all_scramble_word = get_words_scramble(all_original_word)

    return all_original_word, all_scramble_word


def make_dash(word):
    output = ""
    if " " not in word:
        output += "_ " * len(word)
    else:
        this_word = word.split(" ")
        for wrd in this_word:
            output += make_dash(wrd)
            if wrd != this_word[-1]:
                output += "   "
    return output


if __name__ == '__main__':
    original_word, scramble_word = word_scramble("word", how_many_word=0)


