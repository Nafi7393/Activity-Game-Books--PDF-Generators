from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image('pic/ans.png', 0, 0, 8.625)
        self.set_font("helvetica", size=9.5)
        self.cell(w=0, h=0.7, ln=True, border=0)
        self.set_left_margin(0.5)
        self.set_right_margin(0.5)


# Constant variables
margin = 0.378
box_size = 0.18
gap = 1.4


def print_board(pdf, ans1, qus1, ans2, qus2):
    pdf.set_fill_color(200, 200, 200)
    for row in range(20):
        for column in range(20):
            if ans1[row][column] != "_":
                pdf.set_font("helvetica", size=11, style="B")
                pdf.cell(w=box_size, h=box_size, txt=f"{ans1[row][column]}", ln=False, border=0, align="C", fill=True, markdown=True)
            else:
                pdf.set_font("helvetica", size=9.6)
                pdf.cell(w=box_size, h=box_size, txt=f"{qus1[row][column]}", ln=False, border=0, align="C")

        pdf.cell(w=0.42, h=box_size, ln=False, border=0)

        for column in range(20):
            if ans2[row][column] != "_":
                pdf.set_font("helvetica", size=11, style="B")
                pdf.cell(w=box_size, h=box_size, txt=f"{ans2[row][column]}", ln=False, border=0, align="C", fill=True)
            else:
                pdf.set_font("helvetica", size=9.6)
                pdf.cell(w=box_size, h=box_size, txt=f"{qus2[row][column]}", ln=False, border=0, align="C")
        pdf.cell(w=0, h=box_size, ln=True, border=0)


def make_ans_pdf():
    import QUS_ANS_CONTAINER
    answers = QUS_ANS_CONTAINER.ans
    questions = QUS_ANS_CONTAINER.qus

    total_qus = len(answers) // 2

    pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

    pdf.set_auto_page_break(auto=True)
    pdf.author = "Nikolas A. Wit"
    pdf.add_page()

    for i in range(total_qus):
        number = i
        number += i

        print_board(pdf, answers[number], questions[number], answers[number + 1], questions[number + 1])
        pdf.set_font("helvetica", size=14, style="B")
        pdf.cell(w=3.6, h=0.5, txt=f"WORD SEARCH #{number + 1}", ln=False, border=0, align="C")
        pdf.cell(w=0.42, h=0.5, txt=f"", ln=False, border=0, align="C")
        pdf.cell(w=3.6, h=0.5, txt=f"WORD SEARCH #{number + 2}", ln=True, border=0, align="C")
        pdf.cell(w=0, h=gap - 0.5, ln=True)
    pdf.output("ANSWER.pdf")


if __name__ == '__main__':
    make_ans_pdf()