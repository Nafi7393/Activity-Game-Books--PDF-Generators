import random
import popper


def make_symmetry_sudoku(box):
    box1, box2, box3, box4, box5, box5_2, box6, box7, box8, box9 = popper.all_box()
    big_box = []
    choice_num_for_big_box = box

    def make_symmetry(box__1, box__2, choice):
        grid_size = len(box__1)
        how_many_num = random.choice(choice)
        popper_list_for_box__1 = []
        popper_list_for_box__2 = []

        for popper_num in range(grid_size - how_many_num):
            pop_num = random.choice(box__1)
            while pop_num in popper_list_for_box__1:
                pop_num = random.choice(box__1)

            popper_list_for_box__1.append(pop_num)
            big_box.append(pop_num)
        box__2.reverse()
        for i in popper_list_for_box__1:
            index_num = box__1.index(i)
            popper_list_for_box__2.append(box__2[index_num])
            big_box.append(box__2[index_num])

    def for_box5():
        for_box_5 = random.choice([2, 2, 3])
        final_box = []
        popper_list_for_box5 = []
        popper_list_for_box5_2 = []
        for popper_num in range(for_box_5):
            pop_num = random.choice(box5)
            while pop_num in popper_list_for_box5:
                pop_num = random.choice(box5)

            popper_list_for_box5.append(pop_num)

        box5_2.reverse()
        for i in popper_list_for_box5:
            index_num = box5.index(i)
            popper_list_for_box5_2.append(box5_2[index_num])
            final_box.append(i)
            final_box.append(box5_2[index_num])

        for k in box5:
            if k in final_box:
                pass
            else:
                big_box.append(k)

    make_symmetry(box1, box9, choice_num_for_big_box)
    make_symmetry(box2, box8, choice_num_for_big_box)
    make_symmetry(box3, box7, choice_num_for_big_box)
    make_symmetry(box4, box6, choice_num_for_big_box)
    for_box5()

    return big_box

