from fpdf import FPDF

import functions
import skyscraper


class PDF(FPDF):
    def header(self):
        pdf.image("pics/qus_must.png", 0, 0, 8.625)


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.450
text_margin = 0.375

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.set_margin(margin)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=12)
pdf.add_page()


def print_sky(this_one, answer, stay, row, column, box_size, extra):
    if this_one[row][column] != 0:
        if row == 0 or row == 10:
            pdf.cell(w=box_size, h=box_size + extra, txt=f"{this_one[row][column]}", ln=False, border=0, align="C")
        else:
            pdf.cell(w=box_size + extra, h=box_size, txt=f"{this_one[row][column]}", ln=False, border=0, align="C")
    elif row == 0 or row == 10:
        pdf.cell(w=box_size + extra, h=box_size, txt=f" ", ln=False, border=0, align="C")
    else:
        if [row - 1, column - 1] in stay:
            pdf.cell(w=box_size, h=box_size, txt=f"{answer[row - 1][column - 1]}", ln=False, border=1, align="C")
        else:
            pdf.cell(w=box_size, h=box_size, txt=f" ", ln=False, border=1, align="C")


def make_qus_page(page_num, show_num, qus_output_name="qus"):
    page_num *= 6
    ans_list = []
    box_size = 0.28
    extra = box_size / 2
    between_gap = 1
    up_gap = 0.3

    count = 0
    page_number = 0

    for i in range(page_num):
        sky_number = i
        if sky_number == i:
            sky_number += i

        pdf.cell(w=0, h=up_gap, ln=True, border=0)

        ans_grid, qus_grid = skyscraper.make_skyscraper()
        ans_grid2, qus_grid2 = skyscraper.make_skyscraper()

        ans_list.append(ans_grid)
        ans_list.append(ans_grid2)

        stay = functions.pic_this_many_positions(show_num)
        stay2 = functions.pic_this_many_positions(show_num)

        for row in range(11):
            for column in range(11):
                print_sky(qus_grid, ans_grid, stay, row, column, box_size, extra)
            pdf.cell(w=between_gap)
            for column in range(11):
                print_sky(qus_grid2, ans_grid2, stay2, row, column, box_size, extra)

            if row == 0:
                pdf.cell(w=0, h=box_size + extra, ln=True)
            else:
                pdf.cell(w=0, h=box_size, ln=True)

        pdf.cell(w=0, h=0.1, txt=f" ", ln=True, border=0, align="C")
        pdf.cell(w=0.37 * 9, h=0.33, txt=f"Skyscraper #{sky_number + 1}", ln=False, border=0, align="C")
        pdf.cell(w=1.05, h=0.33, txt=f" ", ln=False, border=0, align="C")
        pdf.cell(w=0.37 * 9, h=0.33, txt=f"Skyscraper #{sky_number + 2}", ln=True, border=0, align="C")

        count += 1
        if count == 2:
            count = 0
            page_number += 1
            print(f"{page_number} No. Page Done")

        pdf.cell(w=0, h=between_gap + 0.22, ln=True, border=0)

    with open("ans_container.txt", "w") as output:
        output.write(str(ans_list))

    pdf.output(f"{qus_output_name}.pdf")


if __name__ == '__main__':
    make_qus_page(page_num=5, show_num=21)







































