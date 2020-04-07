# Program sprawdza czy podana liczba jest liczbą parzystą czy nieparzystą.
def even_number():
    try:
        x = int(input('Podaj liczbę:'))
        if x % 2 == 0:
            print('Liczba jest parzysta!')
        else:
            print('Liczba jest nieparzysta!')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        even_number()

