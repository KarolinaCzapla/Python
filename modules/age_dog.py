# Program przelicza wiek psa na wiek człowieka



def age_dog():
    try:
        year_dog = int(input('Wpisz wiek psa(w latach):'))
        if year_dog > 2:
            age = 21 + (year_dog - 2) * 4
        else:
            age = year_dog * 10.5
        print(f'Wiek psa w ludzkich latach wynosi {age}')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        age_dog()




