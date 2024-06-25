from PIL import Image, ImageDraw, ImageFont
from random import shuffle
from os import mkdir, walk
from shutil import rmtree
import textwrap


MAX_W = 900
MAX_H = 600


def get_lines():
    all_lines = []

    with open("_lines.txt", "r", encoding="utf8") as lines:
        for line in lines:
            line = line.upper().replace("WOULD YOU RATHER ", "").strip("\n")
            line = line.replace("’", "'").replace('”', '"').replace('“', '"')
            all_lines.append(line)
    shuffle(all_lines)
    return all_lines


def remove_previous():
    rmtree("questions")
    mkdir("questions")


def make_qus_images():
    all_lines = get_lines()
    remove_previous()

    for i in range(len(all_lines)):
        font = ImageFont.truetype('essential/SANDBOX TTF.ttf', 50)
        txt = all_lines[i]

        if len(txt) <= 35:
            current_h = 170
            width = 18
            font = ImageFont.truetype('essential/SANDBOX TTF.ttf', 60)
        elif len(txt) > 100:
            current_h = 150
            width = 35
            font = ImageFont.truetype('essential/SANDBOX TTF.ttf', 40)
        else:
            current_h = 150
            width = 28

        img = Image.new(mode="RGB", size=(MAX_W, MAX_H), color="white")
        draw = ImageDraw.Draw(img)

        para = textwrap.wrap(txt, width=width)

        pad = 18
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill="black")
            current_h += h + pad

        rgba = img.convert("RGBA")
        img_data_all = rgba.getdata()
        new_data = []
        for item in img_data_all:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        rgba.putdata(new_data)

        im2 = Image.open("essential/back.png").convert("RGBA")
        im2.paste(rgba, (0, 0), rgba)
        im2.save(f'questions/{i + 1}.png', "PNG")


def get_question_files():
    make_qus_images()
    filenames = next(walk("questions"), (None, None, []))[2]  # [] if no file
    return filenames












