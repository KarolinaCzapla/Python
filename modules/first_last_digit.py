# Program wyświetla pierwszą i ostatnią cyfrę w liczbie.


def first_last_digit():
    try:
        number = int(input('Podaj liczbę: '))
        number = str(number)
        print(f'Pierwsza cyfra to:  {number[0]}')
        print(f'Ostatnia cyfra to: {number[-1]}')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
first_last_digit()



