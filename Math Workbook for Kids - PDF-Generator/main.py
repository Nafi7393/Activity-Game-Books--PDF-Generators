from fpdf import FPDF
import random

margin = 0.380
text_margin = 0.390


class PDF(FPDF):

    def header(self):
        self.image("bg.jpg", 0, 0, 8.625)
        self.set_line_width(0.04)
        self.set_margins(left=margin + 0.2, top=margin + 0.1, right=margin + 0.2)
        self.set_font("helvetica", "B", 18)
        self.cell(w=0, h=0.5, border=0, txt="Name:___________________                 Date:___/___/_____",
                  ln=True, align="C")

    def footer(self):
        self.set_y(-0.8)
        self.set_font("helvetica", "I", 12)
        self.cell(w=0, h=0.5, txt=f"Exercise -    {self.page_no()} / {{nb}}", border=0, align="C")


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))
pdf.author = "Benjamin G. Howlett"
pdf.add_page()
pdf.set_font("helvetica", size=16)


def make_addition(number, minimum, maximum, operator="+", want_negetive_number_as_result="NO"):
    answers = []
    max_qus_in_row = 2
    max_ans_in_row = 4
    max_in_a_page = 20
    total_page = number
    maximum = maximum + 1
    want_negetive_number_as_result = want_negetive_number_as_result.lower()

    for i in range(total_page):
        for total_number in range(max_in_a_page):
            first_num = random.randrange(minimum, maximum)
            second_num = random.randrange(minimum, maximum)

            if operator == "+" or operator == "-" or operator == "*" or operator == "x" or operator == "X":

                if operator == "+":
                    pdf.cell(w=4, h=text_margin + 1, txt=f"{total_number + 1}.)    {first_num} + {second_num} = ",
                             ln=False, border=0, align="L")

                    answer =f"{total_number + 1}.) {first_num + second_num}"
                    answers.append(answer)

                if operator == "-":
                    if want_negetive_number_as_result == "no":
                        while second_num > first_num:
                            second_num = random.randrange(minimum, maximum)

                    pdf.cell(w=4, h=text_margin + 1, txt=f"{total_number + 1}.)    {first_num} - {second_num} = ",
                             ln=False, border=0, align="L")

                    answer =f"{total_number + 1}.) {first_num - second_num}"
                    answers.append(answer)

                if operator == "*" or operator == "x" or operator == "X":
                    pdf.cell(w=4, h=text_margin + 1, txt=f"{total_number + 1}.)    {first_num} x {second_num} = ",
                             ln=False, border=0, align="L")

                    answer =f"{total_number + 1}.) {first_num * second_num}"
                    answers.append(answer)

            if operator == "/":
                while True:
                    second_num = random.randrange(minimum, maximum)
                    if first_num % second_num == 0:
                        break

                pdf.cell(w=4, h=text_margin + 1, txt=f"{total_number + 1}.)    {first_num} ÷ {second_num} = ",
                         ln=False, border=0, align="L")

                answer = f"{total_number + 1}.) {round((first_num / second_num))}"
                answers.append(answer)

            max_qus_in_row -= 1
            if max_qus_in_row == 0:
                pdf.cell(w=0, h=text_margin + 0.08, txt=f" ", ln=True, border=0, align="C")
                max_qus_in_row = 2
        pdf.cell(w=0, h=text_margin + 0.08, txt=f" ", ln=True, border=0, align="C")
        for ans in answers:
            pdf.cell(w=2, h=text_margin + 2.1, txt=f"{ans}", ln=False, align="L", border=0)
            max_ans_in_row -= 1
            if max_ans_in_row == 0:
                pdf.cell(w=0, h=text_margin + 0.05, txt=f" ", ln=True, border=0, align="C")
                max_ans_in_row = 4

        answers = []
        max_ans_in_row = 4
        pdf.cell(w=0, h=text_margin + 0.9, txt=f" ", ln=True, border=0, align="C")


def lets_make_pdf():
    page_num = int(input("How Many Pages you want?  "))
    min_input_num = int(input("Set a minimum number:  "))
    max_input_num = int(input("Set a maximum number:  "))
    user_givven_op = str(input("Which operator you want? (+, -, *, /):  "))
    negetive_result = "no"
    if user_givven_op == "-":
        negetive_result = str(input("Do you want negetive Numbers (yes/no):  "))
    pdf_name = str(input("Set the out put name:  "))

    make_addition(number=page_num,
                  minimum=min_input_num,
                  maximum=max_input_num,
                  operator=user_givven_op,
                  want_negetive_number_as_result=negetive_result)
    pdf.output(f"{pdf_name}.pdf")


def if_main():
    make_addition(10, 1, 1000, "*")
    pdf.output("test.pdf")


lets_make_pdf()


