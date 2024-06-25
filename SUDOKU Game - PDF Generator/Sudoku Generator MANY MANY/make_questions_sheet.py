from fpdf import FPDF
import suduko
import functions


class PDF(FPDF):
    def header(self):
        self.set_margins(left=0.713, top=margin)
        self.image("bgs/qus_ess.jpg", 0, 0, 8.625)

    def footer(self):
        self.set_font("courier", "B", size=20)
        self.set_y(-1)
        self.cell(w=0, h=text_margin, txt=f" ", align="C")


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.378
text_margin = 0.370

# pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=15)
pdf.add_page()


def make_sudoku_now(total_page_num, min_visible_num, qus_output_name):
    all_answers = []
    total_num = total_page_num * 2
    box_size = 0.36
    done = 0
    contain = 2
    for total in range(total_num):
        sudoku_number = total
        if sudoku_number == total:
            sudoku_number += total

        pdf.cell(w=0, h=box_size * 1.2, txt=f"", ln=True, border=0)

        qus_grid, ans_grid = suduko.make_sudoku(minimum_visible_num=min_visible_num) #17 have to be must for a valid sudoku
        qus_grid_2, ans_grid_2 = suduko.make_sudoku(minimum_visible_num=min_visible_num) #17 have to be must for a valid sudoku

        for row in range(9):
            for column in range(9):
                if qus_grid[row][column] == 0:
                    pdf.cell(w=box_size, h=box_size, txt=f" ", border=1, ln=False, align="C")
                else:
                    pdf.cell(w=box_size, h=box_size, txt=f"{qus_grid[row][column]}", border=1, ln=False, align="C")

            pdf.cell(w=box_size*2, h=box_size, ln=False)

            for column in range(9):
                if qus_grid_2[row][column] == 0:
                    pdf.cell(w=box_size, h=box_size, txt=f" ", border=1, ln=False, align="C")
                else:
                    pdf.cell(w=box_size, h=box_size, txt=f"{qus_grid_2[row][column]}", border=1, ln=False, align="C")

            pdf.cell(w=0, h=box_size, ln=True)

        pdf.cell(w=box_size * 9, h=box_size, txt=f"Sudoku #{sudoku_number+1}", ln=False, border=0, align="C")
        pdf.cell(w=0.72, h=box_size, txt=f" ", ln=False, border=0, align="C")
        pdf.cell(w=box_size * 9, h=box_size, txt=f"Sudoku #{sudoku_number+2}", ln=True, border=0, align="C")

        all_answers.append(ans_grid)
        all_answers.append(ans_grid_2)

        contain -= 1
        pdf.cell(w=0, h=box_size * 2.8, txt=f"", ln=True, border=0)

        if contain == 0:
            contain = 2
            done += 1
            print(f"Done {done}")

    with open("ans_container.txt", "w") as output:
        output.write(str(all_answers))
    pdf.output(f"{qus_output_name}.pdf")
    return True


if __name__ == "__main__":
    number = 1
    how_many_pages = number * 3
    make_sudoku_now(how_many_pages, min_visible_num=27, qus_output_name="TEST_QUESTIONS")
    # minimum_visible_num must have minimum value of 17 and cannot be higher than 81

