from fpdf import FPDF
import json


class PDF(FPDF):
    def header(self):
        self.image("pics/ans_must.png", 0, 0, 8.625)
        self.set_margins(left=0.87, top=margin)
        self.set_font("helvetica", size=20)
        self.cell(w=0, h=text_margin + 0.13, txt="A N S W E R S", align="C", ln=True)
        self.set_line_width(0.022)
        self.line(3, 0.82, 5.63, 0.82)


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.378
text_margin = 0.370

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=9)
pdf.add_page()


def solution(ans_output_name="ans"):
    with open("ans_container.txt", "r") as answers:
        sky_answers = json.loads(answers.read())

    total_sudo = len(sky_answers)
    height = 0.2
    sudo_distance = 0.63
    answer_num = 0

    for ans_num in range(round(total_sudo/3)):
        if ans_num == 0:
            pass
        if ans_num > 0:
            answer_num += 3

        pdf.cell(w=0, h=0.3, ln=True, border=0)
        for row in range(9):
            for column in range(9):
                pdf.cell(w=height, h=height, txt=f"{sky_answers[answer_num][row][column]}", border=1, align="C", ln=False)
            pdf.cell(w=sudo_distance + 0.112, h=height, ln=False, border=0)

            for column in range(9):
                pdf.cell(w=height, h=height, txt=f"{sky_answers[answer_num + 1][row][column]}", border=1, align="C", ln=False)
            pdf.cell(w=sudo_distance + 0.112, h=height, ln=False, border=0)

            for column in range(9):
                pdf.cell(w=height, h=height, txt=f"{sky_answers[answer_num + 2][row][column]}", border=1, align="C", ln=False)
            pdf.cell(w=height, h=height, ln=True)

        pdf.cell(w=1.8, h=0.25, txt=f"Skyscraper #{answer_num + 1}",  ln=False, border=0, align="C")
        pdf.cell(w=0.743, h=0.25, txt=f"",  ln=False, border=0)
        pdf.cell(w=1.8, h=0.25, txt=f"Skyscraper #{answer_num + 2}",  ln=False, border=0, align="C")
        pdf.cell(w=0.743, h=0.25, txt=f"",  ln=False, border=0)
        pdf.cell(w=1.8, h=0.25, txt=f"Skyscraper #{answer_num + 3}",  ln=True, border=0, align="C")
        pdf.cell(w=0, h=0.05, ln=True, border=0)

    pdf.output(f"{ans_output_name}.pdf")


if __name__ == "__main__":
    solution("ans")
