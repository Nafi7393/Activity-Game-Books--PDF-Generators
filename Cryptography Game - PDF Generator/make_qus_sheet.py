import make_crypto
from fpdf import FPDF


class PDF(FPDF):
    pass


pdf = PDF(orientation="P", unit="in", format=(8.625, 11.25))

# Constant variables
margin = 0.378
text_margin = 0.370

pdf.set_auto_page_break(auto=True, margin=margin + 0.1)
pdf.author = "Nikolas A. Wit"
pdf.set_font("helvetica", size=12)
pdf.add_page()


def get_original_and_crypto_lines(word_file_name="lines.txt"):
    all_original_lines = make_crypto.set_all_lines(word_file_name=word_file_name)
    all_cryptoo_lines = []
    for total_lines in range(len(all_original_lines)):
        random_string, correct_string = make_crypto.make_random_strings()
        all_cryptoo_lines.append(make_crypto.make_crypto(all_original_lines[total_lines],
                                                         random_string, correct_string))

    return all_original_lines, all_cryptoo_lines, correct_string


def lets_make_crypto(word_file, output_name="test"):
    height = 0.3
    original_lines, cryptography_lines, all_str = get_original_and_crypto_lines(word_file_name=word_file)
    total_sentence = len(original_lines)
    for line in range(len(cryptography_lines)):
        pdf.cell(w=0.3, h=height, txt=f"{line + 1})", ln=False, border=0)
        pdf.multi_cell(w=0, h=height, txt=cryptography_lines[line], ln=True, border=0)
        pdf.cell(w=0, h=height*4, txt=f" ", ln=True)

    pdf.output(f"{output_name}.pdf")


if __name__ == "__main__":
    lets_make_crypto(word_file="lines.txt")
