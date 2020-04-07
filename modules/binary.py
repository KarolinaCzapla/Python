# Program przelicza liczbę binarną na dziesiętną.
def binary():
    try:
        number = int(input('Podaj liczbe w zapisie binarnym(0/1): '))
        number_len = len(str(number))
        if number_len != 6:
            print('Liczba musi zawierać 6 cyfr !')
        else:
            x = 0
            y = 0
            while number > 0:
                y += 2 ** x * (number % 10)
                number //= 10
                x += 1
            print(f'Podana liczba binarna w zapisie dziesiętnym to {y}.')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        binary()


