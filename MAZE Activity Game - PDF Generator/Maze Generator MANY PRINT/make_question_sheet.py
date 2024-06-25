from fpdf import FPDF
import maze_generator
import shutil
import os
import copy


class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.400
text_margin = 0.370
image_num = 0

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=12)
pdf.add_page()


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


def make_pages(many_page):
    many_maze = many_page * 12
    many_page = many_page * 6
    remove_previous()
    maze_generator.make_this_many_mazes(how_many=many_maze)
    qus_names = get_question_files()

    x = 0.55
    y = 0.6
    solution_num = 0

    x_gap = 4.1
    y_gap = 5.15

    start_x = x
    start_y = y
    size = 3.45
    each_page = 0
    page_count = 0

    for i in range(many_page):
        for maze_ in range(2):
            pdf.image(f"maze_qus/{qus_names[solution_num]}", start_x, start_y, size)
            pdf.set_xy(start_x, start_y + 3.45)
            pdf.cell(w=size, h=0.3, txt=f"Maze #{solution_num + 1}", border=0, ln=True, align="C")
            pdf.set_xy(start_x, start_y)
            start_x += x_gap
            each_page += 1
            solution_num += 1

        start_x = x
        start_y += y_gap
        if each_page == 4 and i != many_page - 1:
            pdf.add_page()
            start_x = x
            start_y = y
            each_page = 0
            page_count += 1
            print(f"{page_count} No. Page DONE")
        elif i == many_page - 1:
            print(f"{page_count + 1} No. Page DONE")

    pdf.output("qus.pdf")


if __name__ == '__main__':
    make_pages(5)

