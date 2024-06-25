from fpdf import FPDF
from os import walk
import copy


class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.44
text_margin = 0.44

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=14)
pdf.add_page()


def get_solution_files():
    start = 1
    sorted_file = []
    filenames = next(walk("maze_ans"), (None, None, []))[2]  # [] if no file
    re_checker = copy.copy(filenames)
    while re_checker:
        for file in filenames:
            if str("solution" + str(start) + ".png") == file:
                sorted_file.insert(0, file)
                start += 1
                re_checker.remove(file)
    sorted_file.reverse()
    return sorted_file


def make_solution_pages():
    file_names = get_solution_files()
    total_solutions = len(file_names)
    solution_num = 0
    x = 0.58
    y = 0.4

    start_x = x
    start_y = y
    size = 2.1
    each_page = 0

    for i in range(total_solutions // 3):
        for solution in range(3):
            pdf.image(f"maze_ans/{file_names[solution_num]}", start_x, start_y, size)
            pdf.set_xy(start_x + 0.65, start_y + 2.18)
            pdf.write(txt=f"Maze #{solution_num + 1}")
            pdf.set_xy(start_x, start_y)
            start_x += 2.7
            each_page += 1
            solution_num += 1

        start_x = x
        start_y += 2.6
        if each_page == 12 and i != (total_solutions // 3) - 1:
            pdf.add_page()
            start_x = x
            start_y = y
            each_page = 0

    pdf.output("ans.pdf")


if __name__ == '__main__':
    make_solution_pages()
