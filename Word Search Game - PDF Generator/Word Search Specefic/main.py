import make_qus
import make_ans

total_ans_pages = int(input("How many answer page you want?\n1 means total of 5 pages\n"))

all_available_orientations = ['left_to_right', 'up_to_down', 'right_to_left', 'down_to_up', 'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left']

#  'left_to_right', 'right_to_left', 'up_to_down', 'down_to_up',
#  'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left'

make_qus.make_qus_pdf(total_ans_pages, 20, all_available_orientations)
make_ans.make_ans_pdf()