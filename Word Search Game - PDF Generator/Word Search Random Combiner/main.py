import make_qus_sheet
import make_ans_sheet


all_available_orientations = ['left_to_right', 'right_to_left', 'up_to_down', 'down_to_up', 'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left']

#  'left_to_right', 'right_to_left', 'up_to_down', 'down_to_up', 'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left'



grid__size = 20
total_ans_pages = int(input("How many answer page you want?\nchoosing 1 means you will have total of 5 Pages\n"))

print(f"***THIS MANY ({total_ans_pages * 4}) QUESTION PAGES YOU WILL GET, AND {total_ans_pages} THIS MANY\nANSWER PAGES")

make_qus_sheet.make_word_search(total_ans_page_num=total_ans_pages,
                                grid_size=grid__size,
                                all__orientations=all_available_orientations,
                                per_page_this_many_words=20,
                                same_word_repate="yes",
                                output_name="_QUESTIONS")


make_ans_sheet.make_ans_pdf()

