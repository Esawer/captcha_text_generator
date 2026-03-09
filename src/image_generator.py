import hashlib
import os
import random
from random import randint

from PIL import Image, ImageDraw, ImageFont, ImageChops, \
    ImageFilter  # importy z biblioteki PIL, która odpowiada za tworzenie obrazów

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # zmienna ścieżki do pliku, stworzona za pomocą modułu os


def encrypt_codes(str_combinations: dict):
    """
    Funkcja odpowiada za haszowanie ciągów znaków - przy pomocy biblioteki hashlib - wykorzystujemy sha512.
    Każdy ciąg znaku jest hashowany - po dodatkowym 'wyczyszczeniu' z niewidzialnych znaków i spacji (dla bezpieczeństwa).
    Po powyższym hashe i ich indexy zostają zapisane w pliku - captcha_codes.txt.

    :param str_combinations: zmienna słownikowa, przechowująca ciągi znaków i indeksów: index;ciąg_znaków

    ##############################
    W tej funkcji AI w większości pisało kod - jeśli chodzi o samą bibliotekę hashlib.
    Nigdy chyba nie używałem hashowania w języku Python - raz w Javie - nie znałem składni ani jak używać hashlib.
    ##############################
    """
    global BASE_DIR
    file_location = BASE_DIR

    try:  # edycja ścieżki file_location
        file_location += "\\web_page\\static"
    except FileNotFoundError or PermissionError:
        file_location += "\\web_page"

    for i, j in enumerate(
            str_combinations.values()):  # proces hashowania w pętli, ciąg znaków jest 'czyszczony' i hashowany w sha512.
        str_combinations[f"{i}"] = hashlib.sha512(j.strip('\n').strip(" ").encode()).hexdigest()

    with open(f"{file_location}\\captcha_codes.txt", 'w') as f:  # zapis hashów do pliku captcha_codes.txt.
        for i, j in enumerate(str_combinations.values()):
            f.write(f"{i};{j}\n")


def create_images(IMG_NUMBER: int):
    """
    Funkcja wpierw przygotowuje ścieżki - plików i obrazów.
    Następnie dochodzi do oczyszczenia indeksów i pozostawieniu tylko ciągi znaków - surowe - same indeksy są zapewnione
    poprzez zmienną słownika.
    Po przejściu do głownej pętli, gdzie rodzaj obraz wraz z zniekształceniami jest generowany, a następnie zapisywany w folderze.

    :param IMG_NUMBER:  ilość obrazów jaka ma być wygenerowana - jest taka sama jak ilość ciągów znaków.
    ##############################
    W tej funkcji używałem dużo AI, zawsze do biblioteki PIL, nigdy w niej nie pisałem a dokumentacja jest trudna i ubłoga.
    Nie było w niej informacji jak np. narysować linę - AI to wiedziało.
    Samo ustawienie efektów (ich mocy) jest moje, lecz ich implementacja (jak je napisać) zostały zrobione przez AI.
    ##############################
    """
    global BASE_DIR  # zmienna ścieżki do pliku, stworzona za pomocą modułu os
    file_location = os.path.dirname(BASE_DIR)
    img_location = os.path.dirname(BASE_DIR)

    try:  # ścieżki do pliku z ciągami znaków i do obrazów.
        file_location += "\\src\\web_page\\static\\captcha_codes.txt"
        img_location += "\\src\\web_page\\static\\captcha_images"

    except FileNotFoundError or PermissionError:
        file_location += "\\web_page\\static\\captcha_codes.txt"
        img_location += "\\web_page\\static\\data\\captcha_images"

    str_combinations = dict()  # zmienna słownikowa
    reverse_colors = False  # zmienna bool (ture/false), która decyduej o kolorze - białym lub czarnym - tekstu i obrazu (jeśli tekst jest biały to obraz jest czarny i vice versa)
    color = ['white', 'black']  # tablica 2 elementowa - kolor biały i czarny

    with open(file_location, 'r') as f:  # zmienna słownikowa, wypełnienie
        for i in range(IMG_NUMBER):
            line = f.readline().strip("\n").split(";")
            str_combinations[line[0]] = line[1]

    for i in range(IMG_NUMBER):
        reverse_colors = bool(random.randint(0, 2))  # kolor zostaje wybrany losowo z puli color.
        color = sorted(color, reverse=reverse_colors)

        code = list(str_combinations[f"{i}"])  # ciąg znaków wyodrębiony i dany jako string
        text = "".join((code[i] + (random.randint(0, 3) * " ")) for i in range(len(code)))
        # generacja tekstu, pomiędzy znakami jest dodawana losowa ilość spacji 0-3.

        im_width = 350  # szerokość obrazka
        im_height = 75  # wysokość obrazkia
        img = Image.new("L", (im_width, im_height),
                        color[0])  # zmienna obrazka, w danym kolorze, wymiarach i masce (typ L do skali szarości)
        draw = ImageDraw.Draw(img)

        current_x = 10  # pozycja startu 1 znaku
        for j in range(len(text)):
            ft = ImageFont.truetype(["arialbd.ttf", "arialbi.ttf"][(random.randint(0, 1))], random.randint(35, 40))
            # czcionka znaku jest wybierana losowo z chionki arial bold i arial boli italic - wielkość czcionki też jest losowana.
            draw.text((current_x, random.randint(5, 18)), text[j], fill=color[1], font=ft)
            # znak jest rysowany, pozycja current_x, pozycja y losowana, kolor (odwrotny niż obrazek) i czcionka.
            current_x += draw.textlength(text[j], ft)
            # zmienna current_x jest zwiększana o wielkość znaku i właściwej mu czcionki

        for _ in range(random.randint(3,
                                      7)):  # obraz generuje losową liczbę linii z zakresu, linie te przecinają już wygenerowane znaki.
            draw.line((random.uniform(0, im_width), random.uniform(0, im_height), random.uniform(0, im_width),
                       random.uniform(0, im_height)), fill=color[1], width=random.randrange(3, 5))
            # start i koniec linii jest losowany, podobnie szerokość linii - kolor jest taki sam jak tekst

        for _ in range(randint(5000,
                               7000)):  # kulki 'pointy' zniekształcają dodatkowo obraz - losowa ilość, położenie - kolor tekstu
            draw.point(((random.randint(0, im_width)), (random.randint(0, im_height))), fill=color[1])

        noise = Image.effect_noise((350, 75), random.randrange(30, 45))  # dodatkowy efekt szumu, losowa moc

        img = ImageChops.add(img, noise)  # połączenie efektu szumu z obrazem
        img = img.filter(ImageFilter.GaussianBlur(radius=random.uniform(1, 1.5)))  # dodanie filtru rozmycia gaussa.
        img.save(f"{img_location}\\img_{i}.jpg", format="JPEG",
                 optimized=True)  # stworzenie samego obrazu w folderze z właściwą sobie nazwą.

    encrypt_codes(
        str_combinations)  # wywołanie funkcji hashowania obrazów z parametrem, już oczyszczonych z indeksów ciągów znaków.


"""
Projekt: Kody Autoryzacyjne CAPTCHA
Autor: Igor Wróblewski - 177918
Kierunek: Informatyka stosowana 2 rok - stacjonarnie
"""
