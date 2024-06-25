from fpdf import FPDF
import json


class PDF(FPDF):
    def draw_lines(self):
        self.addition_x = 0
        self.addition_y = 0

        for i in range(4):
            # first ome
            self.line((0.928 + self.addition_x), 1.57, (0.928 + self.addition_x), 4.468)  # Making horizontal Lines
            self.line(0.928, (1.57 + self.addition_y), 3.628, (1.57 + self.addition_y))  # Making vertical Lines

            # second one
            self.line((0.928 + 3.9 + self.addition_x), 1.57, (0.928 + 3.9 + self.addition_x), 4.468)  # Making horizontal Lines
            self.line((0.928 + 3.9), (1.57 + self.addition_y), (3.628 + 3.886), (1.57 + self.addition_y))  # Making vertical Lines

            # third one
            self.line((0.928 + self.addition_x), (1.57 + 4.6), (0.928 + self.addition_x), (4.468 + 4.6))  # Making horizontal Lines
            self.line(0.928, (1.57 + self.addition_y + 4.6), 3.628, (1.57 + self.addition_y + 4.6))  # Making vertical Lines

            # fourth one
            self.line((0.928 + 3.9 + self.addition_x), (1.57 + 4.6), (0.928 + 3.9 + self.addition_x), (4.468 + 4.6))  # Making horizontal Lines
            self.line((0.928 + 3.9), (1.57 + self.addition_y + 4.6), (3.628 + 3.886), (1.57 + self.addition_y + 4.6))  # Making vertical Lines

            self.addition_x += 0.9
            self.addition_y += 0.966

    def header(self):
        self.set_margins(left=0.92, top=margin)
        self.set_font("helvetica", size=20)
        self.cell(w=0, h=text_margin + 0.13, txt="A N S W E R S", align="C")
        self.set_line_width(0.022)
        self.line(3, 0.82, 5.63, 0.82)

        self.set_line_width(0.03)
        self.draw_lines()


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.378
text_margin = 0.370
sudoku_level = 8    # 35 is Beginner, 20 is Intermediate, 8 is Advanced
all_answers = []

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=12)
pdf.add_page()


def solution(total_num, ans_output_name):
    with open("ans_container.txt", "r") as answers:
        sudoku_answers = json.loads(answers.read())

    each_page_contain = 4
    h_margin = text_margin - 0.05
    the_number_of_sudoku = 1

    for i in range(round(total_num/2)):
        number_sud = i
        if number_sud > 0:
            if number_sud == i:
                number_sud += i

        each_page_contain -= 2

        pdf.cell(w=0, h=1.2, txt=f"", ln=True, border=0)
        for row in range(9):
            for column in range(9):
                pdf.cell(w=0.3, h=h_margin, txt=f"{sudoku_answers[number_sud][row][column]}", border=1, ln=False,
                         align="C")
            pdf.cell(w=1.2, h=h_margin, ln=False, border=0)

            for column in range(9):
                pdf.cell(w=0.3, h=h_margin, txt=f"{sudoku_answers[number_sud + 1][row][column]}", border=1, ln=False,
                         align="C")
            pdf.cell(w=0, h=h_margin, ln=True, border=0)

        pdf.cell(w=(6.6-1.2)/2, h=h_margin+0.2, txt=f"Sudoku - {the_number_of_sudoku}", border=0, ln=False, align="C")
        pdf.cell(w=1.2, h=h_margin, ln=False, border=0)
        pdf.cell(w=(6.6 - 1.2) / 2, h=h_margin+0.2, txt=f"Sudoku - {the_number_of_sudoku + 1}", border=0, ln=True, align="C")
        the_number_of_sudoku += 2
        if each_page_contain == 0:
            pdf.cell(w=0, h=1, txt=f"", ln=True, border=0)
            each_page_contain = 4

    pdf.output(f"{ans_output_name}.pdf")


if __name__ == "__main__":
    solution(1, "TEST_ANSWERS")
