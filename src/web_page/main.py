from operator import index
from src.image_generator import create_images
from src.string_generator import generate_strings
from flask import Flask, render_template, request
import os
import random
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # zmienna ścieżki do pliku, stworzona za pomocą modułu os
IMAGE_NUMBER = 100  # maksymalna ilość obrazów i ciągów które program tworzy, zmienna jest ustawiona na 100
app = Flask(__name__)  # mini-framework Flask
str_combination = dict()  # zmienna słownika ciągów


def get_hashes():
    """
    Funkcja pozyskuje hashe z pliku, a następnie dodaje je do str_combination.
    """
    with open(f"{BASE_DIR}\\static\\captcha_codes.txt", 'r') as f:
        for i in f:
            line = list(i.split(";"))
            str_combination[line[0]] = line[1].strip("\n").strip(" ")


@app.route('/')  # Punk startu po main
def index():
    """
    Funkcja pozyskuje hashe, losuje liczbę (liczba mówi na który obrazek będzie na stronie) i renderuje index.html
    """
    r_number = str(random.randint(0, IMAGE_NUMBER - 1))
    static_path = os.path.join(BASE_DIR, "static", "captcha_images")

    get_hashes()

    return render_template("index.html", r_number=r_number)


@app.route('/login', methods=['POST'])
def login():
    """
    Funkcja logowania, po tym jak użytkownik zwrócił formularz logowania lub kliknoł przycisk odśwież CAPTCHA.
    Jeśli przycisk został kliknięty, wtedy nowa liczba obrazka jest generowana i renderuje się index.html

    W przeciwnym razie pozyskujemy login, kod captcha wprowadzony przez użytkownika i numer captcha.
    Sam kod jest hashowany, tak by sprawdzić czy jest zbieżny z hashem odpowiedzi.
    Jeśli login nie jest pusty (może być jaki kolwiek), hasło jest dłuższe niż 7 znaków (jakiekolwiek) i kod CAPTCHA jest poprawny,
    użytkownik loguje się na stronę - w przeciwnym razie strona jest ponownie renderowana z nowym testem CAPTCHA.

    ##############################
    W tych funkcjach używałem AI (login, index, main) do zagadnień z Flaskiem, jako że nigdy go nie używałem.
    Podobna sytuacja wygląda z kodem HTML i CSS, AI w prawie całości go pisało - obu języków używałem w przeszłości,
    lecz zapomniałem je prawie kompletnie.
    To samo w miejscach gdzie w grę wchodził hashlib.
    ##############################
    """
    action = request.form.get('action')

    if action == 'refresh':  # sprawdzenie czy użyto odświeżenia
        r_number = str(random.randint(0, IMAGE_NUMBER - 1))
        return render_template("index.html", r_number=r_number)  # nowy render jeśli tak

    u_code = request.form.get('u_captcha')  # pozyskanie danych wprowadzonych przez użytkownika
    captcha_number = request.form.get("r_number")
    user_login = request.form.get("u_login")
    logged_in = False
    msg = ''  # zmienna msg, wyświetla informację w przypadku nieudanego zalogowania.

    captcha_code = hashlib.sha512(u_code.encode()).hexdigest()  # odpowiedz użytkownika jest hashowana

    if not logged_in:  # jeśli użytkownik nie jest zalogowany, zostają sprawdzone jego dane
        if user_login is not None and len(request.form.get('u_password')) > 7 and captcha_code == str_combination[
            captcha_number]:
            logged_in = True
        else:  # przy nieudanej próbie msg zmienia wartość
            logged_in = False
            msg = 'failure'

    if logged_in:  # user przechodzi na stronę zalogowania, wita go tam napis 'Cześć, login_użytkownika'
        return render_template("user_page.html", user_login=user_login)
    else:  # w przypadku niepowodzenia, nowy numer obraza jest generowany i renderowany jest index.html
        r_number = str(random.randint(0, IMAGE_NUMBER - 1))
        return render_template("index.html", r_number=r_number, msg=msg)


if __name__ == '__main__':
    if bool(random.randint(0, 1)) or (not os.listdir(f"{BASE_DIR}\\static\\captcha_images")):
        # jeśli folder z obrazkami weryfikacji jest pusty lub gdy zmienna losowa bool zwróci 1, nowe obrazy są losowane.
        generate_strings(IMAGE_NUMBER)
        create_images(IMAGE_NUMBER)

    app.run(debug=False)  # aplikacja zostałą włączona, zaczynamy od funkcji index.

"""
Projekt: Kody Autoryzacyjne CAPTCHA
Autor: Igor Wróblewski - 177918
Informatyka stosowana 2 rok - stacjonarnie
"""
