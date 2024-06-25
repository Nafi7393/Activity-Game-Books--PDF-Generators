from fpdf import FPDF
import scramble


class PDF(FPDF):
    pass


def make_qus(output, max_words=0):
    border = False
    pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

    # Constant variables
    pdf.set_auto_page_break(auto=True, margin=0.5)
    pdf.set_left_margin(0.8)
    pdf.set_top_margin(0.8)
    pdf.author = "Nikolas A. Wit"
    pdf.set_font("helvetica", size=16)
    pdf.add_page()

    height = 0.8
    width = 3.6

    original_word, scramble_word = scramble.word_scramble("word", how_many_word=max_words)
    length = len(scramble_word)

    size = 0.5

    for i in range(length):
        if i + 1 >= 100:
            size = 0.6
        pdf.cell(w=size, h=height, txt=f"{i + 1}.", ln=False, border=border, align="L")
        pdf.cell(w=width - size, h=height, txt=f"{scramble_word[i].upper()}", ln=False, border=border, align="L")
        dash = scramble.make_dash(scramble_word[i])
        pdf.cell(w=width, h=height, txt=f"{dash}", ln=True, border=border, align="L")
        print(f"Done {i+1}")

    pdf.output(f"{output}.pdf")
    return original_word, length


def make_pdf(qus_output, ans_output, maximum_words):
    border = False
    origin_wrd, length = make_qus(output=qus_output, max_words=maximum_words)

    pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

    # Constant variables
    pdf.set_auto_page_break(auto=True, margin=0.5)
    pdf.set_left_margin(0.8)
    pdf.set_top_margin(0.8)
    pdf.author = "Nikolas A. Wit"
    pdf.set_font("helvetica", size=16)
    pdf.add_page()

    height = 0.6
    width = 3.7
    size = 0.5

    for i in range(round(length / 2)):
        num = i
        num += i
        if num + 1 >= 100:
            size = 0.65
        pdf.cell(w=size, h=height, txt=f"{num + 1}.", ln=False, border=border, align="L")
        pdf.cell(w=width-size, h=height, txt=f"{origin_wrd[num].upper()}", ln=False, border=border, align="L")
        if num + 2 >= 100:
            size = 0.65
        pdf.cell(w=size, h=height, txt=f"{num + 2}.", ln=False, border=border, align="L")
        pdf.cell(w=width-size, h=height, txt=f"{origin_wrd[num + 1].upper()}", ln=True, border=border, align="L")

    pdf.output(f"{ans_output}.pdf")


if __name__ == '__main__':
    # max_ = int(input("How many words (0 means all the words from the file)\nElse give an even number: "))
    make_pdf("QUESTION", "ANSWER", maximum_words=0)





























