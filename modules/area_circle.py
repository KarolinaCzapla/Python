# Program oblicza pole powierzchni koła.
def area_circle():
    try:
        n = input('Podaj dlugość promienia: ')  # wprowadzenie kwoty jako stringa
        x = n.replace(",", ".")  # zamiana ewentualnego przecinka na kropke
        radius = float(x)  # zamiana stringa na floata
        area = ((radius ** 2) * 3.14)
        print(f'Pole wynosi {area}')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        area_circle()
