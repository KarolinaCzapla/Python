# Program oblicza czy dany rok jest rokiem przestępnym.



def leap_year():
    try:
        year = int(input('Podaj rok: '))
        if year % 400 == 0:
            print(f'Rok {year} jest rokiem przestępnym.')
        elif year % 100 == 0:
            print(f'Rok {year} nie jest rokiem przestępnym.')
        elif year % 4 == 0:
            print(f'Rok {year} jest rokiem przestępnym.')
        else:
            print(f'Rok {year} nie jest rokiem przestępnym.')

    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        leap_year()

