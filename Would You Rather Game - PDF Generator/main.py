from fpdf import FPDF
import make_imgs


class PDF(FPDF):
    def header(self):
        self.image("essential/qus_back.jpg", 0, 0, 6.125)


def make_pdf():
    pdf = PDF(orientation="P", unit="in", format=(6.125, 9.25))
    all_qus_files = make_imgs.get_question_files()
    total_questions = len(all_qus_files)

    pdf.set_auto_page_break(auto=True, margin=0.420)
    pdf.set_margins(0.500, 0.520, 0.600)
    pdf.author = "Benny A. Wit"
    pdf.add_font('DolphinCandy', '', 'essential/DolphinCandy.ttf', uni=True)
    pdf.set_font("DolphinCandy", size=37)
    pdf.add_page()

    x = 0.6
    y = 0.95

    y_gap = 4.4

    start_x = x
    start_y = y
    size = 5
    each_page = 0

    for i in range(total_questions):
        pdf.set_xy(start_x, start_y - 0.7)
        pdf.cell(w=0, h=1, txt="Would You Rather", border=0, align="C")
        pdf.image(f"questions/{all_qus_files[i]}", start_x, start_y, size)
        start_y += y_gap
        each_page += 1
        if each_page == 2 and i != total_questions - 1:
            each_page = 0
            start_y = y
            pdf.add_page()

    pdf.output("WOULD YOU RATHER.pdf")


if __name__ == '__main__':
    make_pdf()
























