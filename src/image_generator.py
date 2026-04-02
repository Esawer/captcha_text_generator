import hashlib
import os
import random
from random import randint

from PIL import Image, ImageDraw, ImageFont, ImageChops, \
    ImageFilter  # importy z biblioteki PIL, która odpowiada za tworzenie obrazów

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def encrypt_codes(str_combinations: dict):
    """
    This function hashes strings using hashlib and the SHA-512 algorithm.
    Additionally, every string is stripped of newline characters and spaces.
    Finally, the hashes are saved to a text file.

    :param str_combinations: A dictionary containing plaintext strings.

    ##############################
    I used AI to help me with hashlib.
    ##############################
    """
    global BASE_DIR
    file_location = BASE_DIR

    try:
        file_location += "\\web_page\\static"
    except FileNotFoundError or PermissionError:
        file_location += "\\web_page"

    for i, j in enumerate(
            str_combinations.values()):
        str_combinations[f"{i}"] = hashlib.sha512(j.strip('\n').strip(" ").encode()).hexdigest()

    with open(f"{file_location}\\captcha_codes.txt", 'w') as f:
        for i, j in enumerate(str_combinations.values()):
            f.write(f"{i};{j}\n")


def create_images(IMG_NUMBER: int):
    """
    First, strings are stripped of their indices, leaving bare strings
    that are then used for image generation.
    Afterwards, the images are generated using Pillow (PIL).

    :param IMG_NUMBER: The number of images to generate.
    ##############################
    I used AI for the Pillow library work (as I had never used it before).
    ##############################
    """
    global BASE_DIR
    file_location = os.path.dirname(BASE_DIR)
    img_location = os.path.dirname(BASE_DIR)

    try:
        file_location += "\\src\\web_page\\static\\captcha_codes.txt"
        img_location += "\\src\\web_page\\static\\captcha_images"

    except FileNotFoundError or PermissionError:
        file_location += "\\web_page\\static\\captcha_codes.txt"
        img_location += "\\web_page\\static\\data\\captcha_images"

    str_combinations = dict()
    reverse_colors = False  # Boolean; determines the color of both the text and the background.
    color = ['white', 'black']  # Colors of text and background.

    with open(file_location, 'r') as f:
        for i in range(IMG_NUMBER):
            line = f.readline().strip("\n").split(";")
            str_combinations[line[0]] = line[1]

    for i in range(IMG_NUMBER):
        reverse_colors = bool(random.randint(0, 2))
        color = sorted(color, reverse=reverse_colors)

        code = list(str_combinations[f"{i}"])
        text = "".join((code[i] + (random.randint(0, 3) * " ")) for i in range(len(code)))
        # Text generation with a random number of spaces between characters.

        im_width = 350  # Image width.
        im_height = 75  # Image height.
        img = Image.new("L", (im_width, im_height),
                        color[
                            0])  # Image object of the corresponding size, color, and mode ('L' mode is monochrome).
        draw = ImageDraw.Draw(img)

        current_x = 10  # First character starting position.
        for j in range(len(text)):
            ft = ImageFont.truetype(["arialbd.ttf", "arialbi.ttf"][(random.randint(0, 1))], random.randint(35, 40))
            # Font type and size are randomized.
            draw.text((current_x, random.randint(5, 18)), text[j], fill=color[1], font=ft)
            # The character is drawn with a randomized Y position.
            current_x += draw.textlength(text[j], ft)

        for _ in range(random.randint(3,
                                      7)):  # A random number of lines is generated.
            draw.line((random.uniform(0, im_width), random.uniform(0, im_height), random.uniform(0, im_width),
                       random.uniform(0, im_height)), fill=color[1], width=random.randrange(3, 5))
            # The start and end points of the line are randomized.

        for _ in range(randint(5000,
                               7000)):  # Points / grain effect.
            draw.point(((random.randint(0, im_width)), (random.randint(0, im_height))), fill=color[1])

        noise = Image.effect_noise((350, 75), random.randrange(30, 45))  # Noise effect with randomized strength.

        img = ImageChops.add(img, noise)  # The noise effect is added.
        img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(1, 1.5)))  # Gaussian blur.
        img.save(f"{img_location}\\img_{i}.jpg", format="JPEG",
                 optimized=True)  # The image is saved.

    encrypt_codes(
        str_combinations)  # Calls the encryption function with string combinations as the argument.