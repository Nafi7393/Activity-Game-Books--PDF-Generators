import make_question_sheet
import make_solution_sheet

ans_page_num = int(input("How many answer page you want?\n1 means total of 5 pages\n"))
qus_pages = ans_page_num * 4

level = int(input("How Difficult you want:- "))

make_question_sheet.make_pages(many_page=qus_pages, level=level)
make_solution_sheet.make_solution_pages()

