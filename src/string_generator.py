import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_strings(IMG_NUMBER: int):
    """
    Generates random strings and saves them to the `str_combinations` dictionary.
    The function filters out characters that are hard for humans to read or easily confused (e.g., -, _, 1, ~, I, l, ), ().
    If a chosen character is easy to read and not already in the string, it is added; otherwise, the process repeats.
    Each string is composed of 5 to 8 characters.

    :param IMG_NUMBER: The total number of strings to generate.

    ##############################
    I used AI for the random module, as well as for general syntax.
    ##############################
    """

    str_combinations = dict()

    for i in range(IMG_NUMBER):
        n = random.randrange(5, 9)  # Randomized string length.
        comb = ""  # Temporary string placeholder.

        for _ in range(n):
            while True:
                character = random.randint(35,
                                           123)  # If the chosen character is not in the excluded list and not already in the string, it is added.
                if (chr(character) not in
                        ("-", "_", "1", "~", "`", "!", "I", "l",
                         "0", "O", '"', "'", "}", "{", "(", ")",
                         ";", ":", "/", "\\", ",", ".", "[", "]", "i", 't', "&", "=", "+", ">", "<", "j", 'o') and chr(
                            character) not in comb):
                    comb += chr(character)
                    break

        str_combinations[str(i)] = comb  # The generated string is added to the dictionary.

    strings_to_file(str_combinations)  # Calls the strings_to_file function with the dictionary as the argument.


def strings_to_file(str_combinations: dict):
    """
    Opens the captcha_codes.txt file and saves the strings in the following format:
    0;abcde
    1;fghijkm
    2;tfsbrh

    :param str_combinations: A dictionary of strings created by generate_strings().

    ##############################
    I used AI to help me with the os module, as well as for syntax.
    ##############################
    """
    global BASE_DIR
    file_location = BASE_DIR

    try:
        file_location += "\\web_page\\static\\captcha_codes.txt"
    except (FileNotFoundError, PermissionError):
        file_location = BASE_DIR + "\\web_page\\captcha_codes.txt"

    with open(f"{file_location}", 'w') as f:  # Opens the file and saves the strings in the format: index;string
        for i, j in enumerate(str_combinations.values()):
            f.write(f"{i};{j}\n")
