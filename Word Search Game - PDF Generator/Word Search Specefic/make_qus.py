from fpdf import FPDF
import word_search


class PDF(FPDF):
    def header(self):
        self.image('pic/qus.png', 0, 0, 8.625)

    def footer(self):
        self.set_font("courier", "B", size=16)
        self.set_y(-0.8)
        self.cell(w=0, h=margin, txt=f"WORD SEARCH {self.page_no()}", align="C")


# Constant variables
margin = 0.378


def make_qus_pdf(total_ans_page, grid_size, orientations):
    pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

    pdf.set_auto_page_break(auto=True)
    pdf.author = "Nikolas A. Wit"
    pdf.add_page()

    all_ans = []
    all_qus = []

    total_qus_page = total_ans_page * 4
    box_size = 0.32
    top_gap = 1.2
    bottom_gap = 0.34

    for _ in range(total_qus_page):
        pdf.set_font("helvetica", size=16)
        q_grid, a_grid, answers = word_search.make_word_search(grid_size=grid_size, orient=orientations)
        all_ans.append(a_grid)
        all_qus.append(q_grid)

        pdf.cell(w=0, h=top_gap - 0.6, txt="", ln=True, border=0)
        for key in answers.keys():
            key = key[0:-4]
            pdf.cell(w=0, h=0.4, txt=f"{key.upper()}", ln=True, border=0, align="C")
        pdf.cell(w=0, h=0.2, txt="", ln=True, border=0)

        for row in q_grid:
            pdf.cell(w=0.719, h=box_size, txt=f"", ln=False, border=0)
            for wrd in row:
                pdf.cell(w=box_size, h=box_size, txt=f"{wrd}", ln=False, border=0, align="C")
            pdf.cell(w=0.719, h=box_size, txt=f"", ln=True, border=0)
        pdf.cell(w=0, h=bottom_gap, txt="", ln=True, border=0)

        for all_answers in answers.values():
            pdf.set_font("helvetica", size=12.5)
            count = 0
            all_answers.sort()
            for ans in range(20):
                try: pdf.cell(w=1.96, h=0.31, txt=f"{all_answers[ans]}", ln=False, border=0, align="C")
                except: pdf.cell(w=1.96, h=0.31, txt=f"", ln=False, border=0, align="C")
                count += 1
                if count == 4:
                    count = 0
                    pdf.cell(w=0, h=0.31, ln=True)
        if count != 0:
            pdf.cell(w=0, h=0.31, ln=True)

        pdf.cell(w=0, h=top_gap, txt="", ln=True, border=0)
        print(f"Done {_ + 1}")

    with open("QUS_ANS_CONTAINER.py", "w") as q:
        q.write(f"qus = {str(all_qus)}\n")
        q.write(f"ans = {str(all_ans)}")

    pdf.output("QUESTION.pdf")


if __name__ == '__main__':
    all_orientations = ['left_to_right', 'right_to_left', 'up_to_down', 'down_to_up',
                        'diagonal_down_right', 'diagonal_down_left', 'diagonal_up_right', 'diagonal_up_left']
    make_qus_pdf(5, 20, all_orientations)











