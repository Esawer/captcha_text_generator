import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # zmienna ścieżki do pliku, stworzona za pomocą modułu os


def generate_strings(IMG_NUMBER: int):
    """
    Funkcja generuje ciągi znaków, które zostają zapisane w zmiennej słownika - str_combinations.
    Same ciągi wykluczją znaki, które mogą być mylące dla użytkownika - np. - _ 1 ~ I l ) (.
    Sam znak jest wpierw losowany - z danej puli znaków - następnie jeśli znak jest porządany, ten zostaje dodany do danego ciągu znaków,
    w przypadku znaku nieporządanego losowanie jest kontynuowane.
    Sam ciąg znaków może mieć od 5 od 8 znaków - liczba jest losowana.

    Na koniec funkcji dane zmiennej słownika zostają podane jako argument w innej fukcji - strings_to_file.

    :param IMG_NUMBER: liczba ciągów znaków jaką skrypt ma wygenerować

    ##############################
    W samej funkcji nie wykorzystywałem zbytnio AI, jedynie do modułu random - składnia - ten sam efekt osiągnołbym
    czytając dokumentację, lecz jest to bardziej wymagające a efekt jest taki sam.
    Prócz tego możliwe pytania - np. jak 'zrobić' char - używamy chr().
    ##############################
    """

    str_combinations = dict()  # zmienna słownika

    for i in range(IMG_NUMBER):
        n = random.randrange(5, 9)  # losowanie długości ciągu
        comb = ""  # pojedyncza tymczasowa kombinacja

        for _ in range(n):
            while True:
                character = random.randint(35,
                                           123)  # przedział ogólny znaków, następnie ograniczony poprzez kolejny filtr - możnaby użyć regex, jednak go nie znam.
                if (chr(character) not in
                        ("-", "_", "1", "~", "`", "!", "I", "l",
                         "0", "O", '"', "'", "}", "{", "(", ")",
                         ";", ":", "/", "\\", ",", ".", "[", "]", "i", 't', "&", "=", "+", ">", "<", "j", 'o') and chr(
                            character) not in comb):
                    comb += chr(character)  # dodanie znaku do tymczasowej zmiennej kombinacji
                    break

        str_combinations[str(i)] = comb  # dodanie zmiennej kombinacji do str_combinations

    strings_to_file(str_combinations)  # funkcja strings_to_file z argumentem zmiennej słownika


def strings_to_file(str_combinations: dict):
    """
    Funkcja otwiera lub tworzy plik tekstowy captcah_codes.txt, w którym zapisywane są ciągi znaków w następującej formie:
    0;abcde
    1;fghijkm
    2;tfsbrh

    :param str_combinations: zmienna słownikowa zawierająca kombinacje znaków wybranych w funkcji - generate_strings()

    ##############################
    W samej funkcji nie wykorzystywałem zbytnio AI, jedynie do modułu os - dawno go nie używałem.
    Prócz tego może debugowanie ścieżek i dodatkowe pytania.
    ##############################
    """
    global BASE_DIR
    file_location = BASE_DIR  # pochodna od BASE_DIR użyta do ścieżki pliku.

    try:  # samo zachowanie zapisywania plików powinno być zmienione, w przypadku braku folderu, lub zmiany układu projektu program nie będzie działał.
        file_location += "\\web_page\\static\\captcha_codes.txt"
    except FileNotFoundError or PermissionError:
        file_location = BASE_DIR + "\\web_page\\captcha_codes.txt"

    with open(f"{file_location}", 'w') as f:  # otworzenie pliku i zapisanie ciągów znaków: index;ciąg_znaku
        for i, j in enumerate(str_combinations.values()):
            f.write(f"{i};{j}\n")


"""
Projekt: Kody Autoryzacyjne CAPTCHA
Autor: Igor Wróblewski - 177918
Kierunek: Informatyka stosowana 2 rok - stacjonarnie
"""
