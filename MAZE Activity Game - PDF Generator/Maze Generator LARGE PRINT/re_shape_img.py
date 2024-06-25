import numpy as np
from PIL import Image
from cv2 import cv2


def stroke(origin_image, threshold, stroke_size, colors):
    img = np.array(origin_image)
    h, w, _ = img.shape
    padding = stroke_size + 50
    alpha = img[:, :, 3]
    rgb_img = img[:, :, 0:3]
    bigger_img = cv2.copyMakeBorder(rgb_img, padding, padding, padding, padding,
                                    cv2.BORDER_CONSTANT, value=(0, 0, 0, 0))
    alpha = cv2.copyMakeBorder(alpha, padding, padding, padding, padding, cv2.BORDER_CONSTANT, value=0)
    bigger_img = cv2.merge((bigger_img, alpha))
    h, w, _ = bigger_img.shape

    _, alpha_without_shadow = cv2.threshold(alpha, threshold, 255, cv2.THRESH_BINARY)  # threshold=0 in photoshop
    alpha_without_shadow = 255 - alpha_without_shadow
    dist = cv2.distanceTransform(alpha_without_shadow, cv2.DIST_L2, cv2.DIST_MASK_3)  # dist l1 : L1 , dist l2 : l2
    stroked = change_matrix(dist, stroke_size)
    stroke_alpha = (stroked * 255).astype(np.uint8)

    stroke_b = np.full((h, w), colors[0][2], np.uint8)
    stroke_g = np.full((h, w), colors[0][1], np.uint8)
    stroke_r = np.full((h, w), colors[0][0], np.uint8)

    stroke = cv2.merge((stroke_b, stroke_g, stroke_r, stroke_alpha))
    stroke = cv2pil(stroke)
    bigger_img = cv2pil(bigger_img)
    result = Image.alpha_composite(stroke, bigger_img)
    return result


def change_matrix(input_mat, stroke_size):
    stroke_size = stroke_size - 1
    mat = np.ones(input_mat.shape)
    check_size = stroke_size + 1.0
    mat[input_mat > check_size] = 0
    border = (input_mat > stroke_size) & (input_mat <= check_size)
    mat[border] = 1.0 - (input_mat[border] - stroke_size)
    return mat


def cv2pil(cv_img):
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGRA2RGBA)
    pil_img = Image.fromarray(cv_img.astype("uint8"))
    return pil_img


test_image = Image.open("Done.png").convert("RGBA")
img_data_all = test_image.getdata()
new_data = []
for item in img_data_all:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        new_data.append((0, 0, 0, 255))
    else:
        new_data.append(item)
test_image.putdata(new_data)

output = stroke(test_image, threshold=0, stroke_size=15, colors=((255, 255, 255),))
output.show()

