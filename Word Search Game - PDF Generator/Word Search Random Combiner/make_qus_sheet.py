import word_search
from fpdf import FPDF


class PDF(FPDF):

    def header(self):
        self.image('pics/qus_background.png', 0, 0, 8.625)
        self.image('ess_pic/qus.png', 0, 0, 8.625)
        self.set_margins(left=0.533, top=margin + 0.2)

    def footer(self):
        self.set_font("courier", "B", size=18)
        self.set_y(-0.8)
        self.cell(w=0, h=text_margin, txt=f"Word Search {self.page_no()}", align="C")


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.378
text_margin = 0.370

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=14)
pdf.add_page()
all_available_orientations = ['left_to_right', 'right_to_left', 'up_to_down', 'down_to_up',
                              'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left']
# 'left_to_right', 'right_to_left', 'up_to_down', 'down_to_up', 'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left'


def make_word_search(total_ans_page_num, grid_size, all__orientations=all_available_orientations,
                     per_page_this_many_words=20, same_word_repate="no", output_name="test_qus"):

    with open("ans_container.py", "a+") as input_ans:
        input_ans.truncate(0)
        input_ans.write(f"answer = ")

    with open("qus_container.py", "a+") as input_qus:
        input_qus.truncate(0)
        input_qus.write(f"question = ")

    total_page_num = total_ans_page_num * 4
    for total in range(total_page_num):
        pdf.cell(w=7.5, h=0.5, txt=f"", ln=True, border=0)
        answer_grid, answer = word_search.make_word_search(grid_size=grid_size,
                                                        per_page_this_many_words=per_page_this_many_words,
                                                        orientations=all__orientations,
                                                        same_word_repate=same_word_repate)

        with open("ans_container.py", "a+") as output_ans:
            if total != total_page_num - 1:
                output_ans.write(f"{answer_grid},")
            else:
                output_ans.write(f"{answer_grid}")

        question_grid = word_search.make_qus_grid(answer_grid, grid_size)

        with open("qus_container.py", "a+") as output_qus:
            if total != total_page_num - 1:
                output_qus.write(f"{question_grid},")
            else:
                output_qus.write(f"{question_grid}")

        pdf.set_font_size(14)
        for row in range(grid_size):
            pdf.cell(w=0.7, h=0, ln=False, border=0)
            for column in range(grid_size):
                pdf.cell(w=0.309, h=0.309, txt=f"{question_grid[row][column]}", ln=False, border=0, align="C")
            pdf.cell(w=0, h=0.309, txt=f" ", border=0, ln=True)

        pdf.cell(w=0, h=0.35, txt=f"", ln=True, border=0)
        ans_per_row = 4

        answer.sort()
        pdf.set_font_size(13)

        for ans in range(len(answer)):
            pdf.cell(w=1.89, h=0.4, txt=f"{answer[ans]}", ln=False, border=0, align="C")
            ans_per_row -= 1
            if ans_per_row == 0:
                pdf.cell(w=0, h=0.4, txt=f"", ln=True, border=0)
                ans_per_row = 4
        pdf.cell(w=7.5, h=0.8, txt=f"", ln=True, border=0)
        print(f"Done {total + 1} Page")

    pdf.output(f"{output_name}.pdf")


if __name__ == "__main__":
    make_word_search(total_ans_page_num=3, per_page_this_many_words=20, grid_size=20, same_word_repate="yes")  # Grid Size 20 is perfect

