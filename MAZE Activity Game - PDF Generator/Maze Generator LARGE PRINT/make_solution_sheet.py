from fpdf import FPDF
from os import walk
import copy


class PDF(FPDF):
    def header(self):
        self.image('pics/ans_must.png', 0, 0, 8.625)

    def footer(self):
        pass


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.44
text_margin = 0.44

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=16, style="B")
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
    text_box_size = 1
    x = 0.58
    y = 0.8

    start_x = x
    start_y = y
    size = 3.5
    each_page = 0

    for i in range(total_solutions // 2):
        for solution in range(2):
            pdf.image(f"maze_ans/{file_names[solution_num]}", start_x, start_y, size)
            pdf.set_xy(start_x, start_y + size)
            pdf.cell(w=3.5, h=0.5, txt=f"Maze #{solution_num + 1}".upper(), border=False, align="C")
            start_x += 3.9
            each_page += 1
            solution_num += 1

        start_x = x
        start_y += 5.2
        if each_page == 4 and i != (total_solutions // 2) - 1:
            pdf.add_page()
            start_x = x
            start_y = y
            each_page = 0

    pdf.output("ANSWER.pdf")


if __name__ == '__main__':
    make_solution_pages()
