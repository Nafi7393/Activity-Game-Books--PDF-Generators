from fpdf import FPDF
import suduko
import functions


class PDF(FPDF):

    def header(self):
        self.set_margins(left=0.713, top=margin + 0.2)
        self.set_font("helvetica", size=16)
        self.cell(w=7.2 / 2, h=margin + 0.1, txt=f"Player Name:_____________________", border=0, align="L", ln=False)
        self.cell(w=7.2 / 2, h=margin + 0.1, txt=f"Date:___/___/_____", border=0, align="R", ln=True)

        self.set_line_width(0.045)

        self.addition_x = 0
        self.addition_y = 0

        for i in range(4):
            self.line((0.728 + self.addition_x), 1.66, (0.728 + self.addition_x), 8.59)  # Making horizontal Lines
            self.line(0.728, (1.66 + self.addition_y), 7.9, (1.66 + self.addition_y))  # Making vertical Lines
            self.addition_x += 2.391
            self.addition_y += 2.315

    def footer(self):
        self.set_font("courier", "B", size=20)
        self.set_y(-1)
        self.cell(w=0, h=text_margin, txt=f"SUDOKU {self.page_no()}", align="C")


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.378
text_margin = 0.370

# pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=22)
pdf.add_page()


def make_sudoku_now(total_num, minimun_visible_number, qus_output_name):
    all_answers = []
    for total in range(total_num):
        pdf.set_font_size(22)
        pdf.cell(w=0, h=0.6, txt=f"", ln=True)
        running = True
        while running:
            qus_grid, ans_grid = suduko.make_sudoku_pattern(minimun_visible_number)
            for row in range(9):
                for column in range(9):
                    if qus_grid[row][column] == 0:
                        pdf.cell(w=0.8, h=text_margin + 0.4, txt=f" ", border=1, ln=False, align="C")
                    else:
                        pdf.cell(w=0.8, h=text_margin + 0.4, txt=f"{qus_grid[row][column]}", border=1, ln=False, align="C")
                pdf.cell(w=0, h=text_margin + 0.4, ln=True)

            pdf.set_font_size(12)
            pdf.cell(w=(7.2 / 2), h=1, txt=f"Starting Time: _______________________", ln=False, border=0, align="L")
            pdf.cell(w=(7.2 / 2), h=1, txt=f"Ending Time: _______________________", ln=True, border=0, align="R")

            all_answers.append(ans_grid)

            print(f"done {total + 1}")
            break
        pdf.cell(w=0, h=0.8, txt=f"", ln=True)

    with open("ans_container.txt", "w") as output:
        output.write(str(all_answers))
    pdf.output(f"{qus_output_name}.pdf")
    return True


if __name__ == "__main__":
    make_sudoku_now(4, minimun_visible_number=24, qus_output_name="TEST_QUESTIONS")
    # Minimum_visible_num must have minimum value of 17 and cannot be higher than 81

