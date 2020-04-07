# Program  sprawdza czy liczba jest podzielna przez 3 lub 5 lub 7.

def div_number_3or5or7():
    try:
        x = int(input('Podaj liczbę: '))
        if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            print('Liczba jest podzielna!')
        else:
            print('Liczba nie jest podzielna!')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        div_number_3or5or7()

