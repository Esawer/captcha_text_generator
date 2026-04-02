# Captcha Text Generator

[![Polish](https://img.shields.io/badge/Język-Polski-red)](#pl)
[![English](https://img.shields.io/badge/Language-English-blue)](#en)

---
<a id="pl"></a>
## 🔴 Wersja Polska 🔴
Projekt semestralny na kurs **"Bezpieczeństwo systemów informatycznych"** dotyczący kodów weryfikacji CAPTCHA.  
Generowanie ciągów znaków, jak i obrazów z tekstem CAPTCHA bazujących na tych ciągach, które następnie są haszowane.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Library-green?style=for-the-badge)  
![SHA-512](https://img.shields.io/badge/Security-SHA--512-red?style=for-the-badge)

### ⚙️ Działanie i funkcje
1. Po uruchomieniu programu, generowane są alfanumeryczne ciągi znaków - od 5 do 8 znaków - które muszą spełniać kryterium czytelności.
2. Za pomocą biblioteki ***Pillow*** (PIL) tworzone są obrazy z tymi właśnie ciągami znaków.
   * kolor czcionki i obrazu jest losowany - biały lub czarny.
   * rodzaj czcionki tekstu jest losowany (`arialbd`, `arialbi`).
   * rozpiętość liter jest losowa - liczba spacji między znakami i położenie znaków.
   * generowane są losowe linie, które przecinają tekst.
   * dodanie efektu szumu, rozmycia Gaussa i tzw. pointerów, kulek.
3. Gdy obrazy są już wygenerowane, same ciągi znaków są haszowane - SHA-512.
4. Podczas logowania (Flask), użytkownik musi podać poprawną odpowiedź na kod CAPTCHA, jego odpowiedź jest haszowana i jest ona porównywana z zahaszowanym ciągiem znaków.  

**Działanie Programu:** <p align="center">
![Animation1](https://github.com/user-attachments/assets/8a56ad7e-96c9-455c-ab88-1740a785b613)
</p>

**Przykłady wygenerowanych obrazów:** <p align="center">
  <img src="https://github.com/user-attachments/assets/8c310d44-1c17-4b6f-8675-fcc9307875be" alt="img_24">
  <img src="https://github.com/user-attachments/assets/a45c6955-0b5d-42ef-a9fe-24fd6096b366" alt="img_31">
</p>

### 📚 Podejście teoretyczne
Sam projekt został wykorzystany przy stworzeniu 26-stronicowej pracy pisemnej na temat systemów weryfikacji człowieczeństwa:  
* **Teoria** - historia CAPTCHA, krytyka tych systemów i dlaczego nie warto tworzyć własnych systemów weryfikacji człowieczeństwa.  
* **Praktyka** - projekt został opisany, jak i ujęty od strony badawczej, gdzie system weryfikacji był testowany na modelach AI, by sprawdzić jego odporność.

📄 **[Przeczytaj pełną pracę (PDF) tutaj](./captcha_teoria.pdf)**

### 🏭 Struktura Projektu
```text
📦 Katalog główny projektu
├── src/    
│   ├── web_page/  
│   │   ├── static/    
│   │   │   ├── captcha_images/    # Wygenerowane obrazy CAPTCHA  
│   │   │   ├── captcha_codes.txt  # Zahaszowane (SHA-512) kody weryfikacji  
│   │   │   └── style.css          # Arkusze stylów  
│   │   ├── templates/  
│   │   │   ├── index.html         # Strona logowania  
│   │   │   └── user_page.html     # Strona użytkownika 
│   │   └── main.py                # Punkt startowy programu 
│   ├── image_generator.py         # Skrypt renderujący obrazy (Pillow)  
│   └── string_generator.py        # Logika losowania ciągów znaków
├── requirements.txt               # Zależności projektu
└── README.md                      # O projekcie
```

---
<a id="en"></a>
## 🔵 English Version 🔵
Semester project for the **"Security of IT Systems"** course, regarding CAPTCHA verification codes.  
Generating strings that are later used to create CAPTCHA images; the strings themselves are then hashed.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Library-green?style=for-the-badge)  
![SHA-512](https://img.shields.io/badge/Security-SHA--512-red?style=for-the-badge)

### ⚙️ Functions
1. First, random alphanumeric strings - from 5 to 8 characters - are generated, meeting readability standards.
2. With the help of the Pillow (PIL) library, images based on the previous strings are generated:
   * Font and background colors are randomized - either black or white.
   * Font type is randomized (`arialbd`, `arialbi`).
   * Spaces between characters are random; the same applies to their vertical position (higher, lower).
   * Random lines in the same color as the text are generated.
   * Additional effects such as Gaussian blur, pointers/grain, and noise.
3. When the images themselves are ready, the original codes are hashed using SHA-512.
4. When a user wishes to log in, they have to type the correct CAPTCHA verification code - after the program hashes their input, it is compared with the original hashed code. 

**Program in Action:** <p align="center">
![Animation1](https://github.com/user-attachments/assets/8a56ad7e-96c9-455c-ab88-1740a785b613)
</p>

**Examples of generated images:** <p align="center">
  <img src="https://github.com/user-attachments/assets/8c310d44-1c17-4b6f-8675-fcc9307875be" alt="img_24">
  <img src="https://github.com/user-attachments/assets/a45c6955-0b5d-42ef-a9fe-24fd6096b366" alt="img_31">
</p>

### 🏭 Project structure
```text
📦 Project Main Directory
├── src/    
│   ├── web_page/  
│   │   ├── static/    
│   │   │   ├── captcha_images/    # Generated CAPTCHA images  
│   │   │   ├── captcha_codes.txt  # Hashed verification codes (SHA-512)  
│   │   │   └── style.css          # CSS file 
│   │   ├── templates/  
│   │   │   ├── index.html         # Login page  
│   │   │   └── user_page.html     # Sample user page
│   │   └── main.py                # Starting point of the program
│   ├── image_generator.py         # Image generator script (Pillow)  
│   └── string_generator.py        # Random string generator script
├── requirements.txt               # Project requirements
└── README.md                      # About the project
```
