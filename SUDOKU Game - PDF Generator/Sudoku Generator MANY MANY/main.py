import make_questions_sheet
import make_answers_sheet

total_ans_page = int(input("how many answer pages you want?\n1 page means 12 sudoku ans 3 ans pages\n"))
total_sudoku = total_ans_page * 12
total_qus_page = total_ans_page * 3

minimum_visible_number = int(input("how many visible number you want?\n17 is the lowest number you can give and 81 os higher\nless umber means more difficult levels\n"))

make_questions_sheet.make_sudoku_now(total_qus_page, minimum_visible_number, qus_output_name="qus_sheet")
make_answers_sheet.solution(ans_output_name="ans_sheet")

