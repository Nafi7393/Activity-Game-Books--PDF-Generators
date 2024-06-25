from fpdf import FPDF
import maze_generator
import shutil
import os
import copy


class PDF(FPDF):
    def header(self):
        self.image('pics/qus_must.png', 0, 0, 8.625)

    def footer(self):
        self.set_font("helvetica", "B", size=18)
        self.set_y(-0.8)
        self.cell(w=0, h=text_margin, txt=f"Maze #{self.page_no()}", align="C")


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.400
text_margin = 0.370
image_num = 0

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=14)


def remove_previous():
    shutil.rmtree("maze_qus")
    shutil.rmtree("maze_ans")
    os.mkdir("maze_qus")
    os.mkdir("maze_ans")


def get_question_files():
    start = 1
    sorted_file = []
    filenames = next(os.walk("maze_qus"), (None, None, []))[2]  # [] if no file
    re_checker = copy.copy(filenames)
    while re_checker:
        for file in filenames:
            if str("maze" + str(start) + ".png") == file:
                sorted_file.insert(0, file)
                start += 1
                re_checker.remove(file)
    sorted_file.reverse()
    return sorted_file


def make_pages(many_page, level):
    remove_previous()
    maze_generator.make_this_many_mazes(how_many=many_page, size=level)
    qus_names = get_question_files()
    x_pos = 0.58
    y_pos = 1.5
    size = 7.5

    for i in range(many_page):
        pdf.add_page()
        pdf.image(f"maze_qus/{qus_names[i]}", x_pos, y_pos, size)

    pdf.output("QUESTION.pdf")


if __name__ == '__main__':
    make_pages(12, 5)

