# Program sprawdza czy liczba jest podzielne przez 3,5 oraz 7.
def div_number_3a5a7():
    try:
        x = int(input('Podaj liczbę: '))
        if x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
            print('Liczba  jest podzielna!')
        else:
            print('Liczba nie jest podzielna!')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        div_number_3a5a7()
