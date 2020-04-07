import sys
from modules.age_dog import age_dog
from modules.area_circle import area_circle
from modules.binary import binary
from modules.celsius_fahrenheit import celsius_fahrenheit
from modules.coins_change import coins_change
from modules.div_number_3a5a7 import div_number_3a5a7
from modules.div_number_3or5or7 import div_number_3or5or7
from modules.even_number import even_number
from modules.fahrenheit_celsius import fahrenheit_celsius
from modules.first_last_digit import first_last_digit
from modules.leap_year import leap_year
from modules.pyramid import pyramid
from modules.square import square


# from modules.statistics import statistics


def stop():
    print('Koniec programu!')
    exit()


#     answer = input('Chcesz spróbować jeszcze raz (t/n)? ')
#     if answer == 't':
#         menu(programy)
#     elif answer == 'n':
#         print('Koniec programu!')
#         sys.exit(0)


def menu(programs):
    print('MultiTOOL\nMenu:')
    for key, program in programs.items():
        print(f'{key} - {program["name"]}')

    return input('Wpisz cyfre, aby wybrać  program który cię interesuje:').upper()


programs = {
    '1': {'name': 'Program przelicza liczbę binarną na dziesiętną.', 'function': binary},
    '2': {'name': 'Program przelicza stopnie Celsjusza na Fahrenheita.', 'function': celsius_fahrenheit},
    '3': {'name': 'Program przelicza stopnie Fahrenheita na Celsjusza', 'function': fahrenheit_celsius},
    '4': {'name': 'Program przelicza wiek psa na wiek człowieka', 'function': age_dog},
    '5': {'name': 'Program oblicza pole powierzchni koła.', 'function': area_circle},
    '6': {'name': 'Program rozmienia podaną kwote na monety.', 'function': coins_change},
    '7': {'name': 'Program sprawdza czy liczba jest podzielne przez 3,5 oraz 7.', 'function': div_number_3a5a7},
    '8': {'name': 'Program  sprawdza czy liczba jest podzielna przez 3 lub 5 lub 7.', 'function': div_number_3or5or7},
    '9': {'name': 'Program sprawdza czy podana liczba jest liczbą parzystą czy nieparzystą.', 'function': even_number},
    '10': {'name': 'Program wyświetla pierwszą i ostatnią cyfrę w liczbie.', 'function': first_last_digit},
    '11': {'name': 'Program oblicza czy dany rok jest rokiem przestępnym.', 'function': leap_year},
    '12': {'name': 'Program za pomocą znaku # rysuje piramidę.', 'function': pyramid},
    '13': {'name': 'Program rysuje prostokąt o podanych rozmiarach za pomocą znaków +, - , | .', 'function': square},
    # '14': {'name': 'Program pokazuje statystykę dla pliku text.txt.', 'function': statistics},
    'X': {'name': 'Wyjście', 'function': stop},
}
choice = None

while choice != 'X':
    choice = menu(programs)
    try:
        print('=' * 20)
        programs[choice]['function']()
        print('=' * 20)
    except KeyError:
        print('Taki program nie isnieje.')
