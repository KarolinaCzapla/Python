import sys


# Program przelicza liczbę binarną na dziesiętną.
def binary(number):
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


# Program przelicza stopnie Fahrenheita na Celsjusza.
def fahrenheit_celsius(celsius):
    fahrenheit = int(((celsius * 9 / 5) + 32))
    print(f'{celsius} ° Celsjusza to {fahrenheit} ° Fahrenheita.')


# Program przelicza stopnie Celsjusza na Fahrenheita.
def celsius_fahrenheit(fahrenheit):
    celsius = int((fahrenheit - 32.0) * 5 / 9)
    print(f'{fahrenheit} ° Fahrenheita to {celsius} ° Celsjusza')


# Program sprawdza czy liczba jest podzielne przez 3,5 oraz 7.
def div_number_3a5a7(x):
    if x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
        print('Liczba  jest podzielna!')
    else:
        print('Liczba nie jest podzielna!')


# Program  sprawdza czy liczba jest podzielna przez 3 lub 5 lub 7.
def div_number_3or5or7(x):
    if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        print('Liczba jest podzielna!')
    else:
        print('Liczba nie jest podzielna!')


# Program sprawdza czy podana liczba jest liczbą parzystą czy nieparzystą.
def even_number(x):
    if x % 2 == 0:
        print('Liczba jest parzysta!')
    else:
        print('Liczba jest nieparzysta!')


# Program wyświetla pierwszą i ostatnią cyfrę w liczbie.
def first_last_digit(number):
    print('Pierwsza cyfra to: ', number[0])
    print('Ostatnia cyfra to: ', number[-1])


# Program oblicza pole powierzchni koła.
def triangle_area(radius):
    area = ((radius ** 2) * 3.14)
    print(f'Pole wynosi {area}')


# Program rysuje prostokąt o podanych rozmiarach za pomocą znaków +, - , | .
def square(x, y):
    for i in range(0, x):
        for j in range(0, y):
            if i == 0 or i == x - 1:
                if j == 0 or j == y - 1:
                    print("+", end=" ")
                else:
                    print("-", end=" ")
            elif j == 0 or j == y - 1:
                print("|", end=" ")
            else:
                print(" ", end=" ")

        print()


# Program oblicza czy dany rok jest rokiem przestępnym.
def leap_year(year):
    if year % 4 == 0:
        print(f'Rok {year} jest rokiem przestępnym.')
    else:
        print(f'Rok {year} nie jest rokiem przestępnym.')


# Program za pomocą znaku # rysuje piramidę.
def pyramid(width):
    for i in range(0, width):
        for j in range(0, width - i):
            print(" ", end="")
        for k in range(0, 2 * i + 1):
            print("#", end="")
        print("")


# Program przelicza wiek psa na wiek człowieka
def age_dog(year_dog):
    if year_dog > 2:
        age = 21 + (year_dog - 2) * 4
    else:
        age = year_dog * 10.5
    print(f'Wiek psa w ludzkich latach wynosi {age}')


# Program rozmienia podaną kwote na monety.
def coins_change(n):
    coins = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    coins_a = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    i = 0
    z = round(n * 100)
    coins_len = len(coins)
    while z > 0:
        if coins_a[i] > z:
            if i < coins_len:
                i = i + 1
        else:
            z = (z - coins_a[i])
            print(coins[i], end=" PLN    ")


def exit():
    answer = input('Chcesz spróbować jeszcze raz (t/n)? ')
    if answer == 't':
        value_error()
    elif answer == 'n':
        print('Koniec programu!')
        sys.exit(0)
    else:
        print("Podano nieprawidłowe dane! Następnym razem wpisz t lub n. ")
        value_error()


def value_error():
    def one():
        print('Program przelicza liczbę binarną na dziesiętną')
        number = int(input('Podaj liczbe w zapisie binarnym(0/1): '))
        binary(number)
        exit()

    def two():
        print('Program przelicza stopnie Celsjusza na Fahrenheita.\n'
              'Używa do tego wzoru Fahrenheit=((Celsius*9/5)+32.')
        celsius = float(input('Podaj temperaturę w stopniach Celsjusza: '))
        fahrenheit_celsius(celsius)
        exit()

    def three():

        print('Program przelicza stopnie Fahrenheita na Celsjusza.\n'
              'Używa do tego wzoru Celsius = (Fahrenheit – 32) * 5/9.')
        fahrenheit = float(input('Podaj temperaturę w stopniach Fahrenheita: '))
        celsius_fahrenheit(fahrenheit)
        exit()

    def four():
        print('Program sprawdza czy liczba jest podzielne przez 3,5 oraz 7.')
        x = int(input('Podaj liczbę: '))
        div_number_3a5a7(x)
        exit()

    def five():
        print('Program  sprawdza czy liczba jest podzielna przez 3 lub 5 lub 7.')
        x = int(input('Podaj liczbę: '))
        div_number_3or5or7(x)
        exit()

    def six():
        print('Program sprawdza czy podana liczba jest liczbą parzystą czy nieparzystą.')
        x = int(input('Podaj liczbę:'))
        even_number(x)
        exit()

    def seven():
        print('Program wyświetla pierwszą i ostatnią cyfrę w liczbie.')
        number = (input('Podaj liczbę: '))
        first_last_digit(number)
        exit()

    def eigth():
        print('Program oblicza pole powierzchni koła.')
        n = input('Podaj dlugość promienia: ')  # wprowadzenie kwoty jako stringa
        x = n.replace(",", ".")  # zamiana ewentualnego przecinka na kropke
        radius = float(x)  # zamiana stringa na floata
        triangle_area(radius)  # wykonanie funkcji
        exit()

    def nine():
        print('Program rysuje prostokąt o podanych rozmiarach za pomocą znaków +, - , | .')
        x = int(input('Podaj liczbę wierszy: '))
        y = int(input('Podaj liczbę kolumn: '))
        square(x, y)
        exit()

    def ten():
        print('Program oblicza czy dany rok jest rokiem przestępnym.')
        year = int(input('Podaj rok: '))
        leap_year(year)
        exit()

    def eleven():
        print('Program za pomocą znaku # rysuje piramidę.')
        width = int(input('Podaj wysokość piramidy: '))
        pyramid(width)
        exit()

    def twelve():
        print('Program przelicza wiek psa na wiek człowieka.')
        year_dog = int(input('Wpisz wiek psa(w latach):'))
        age_dog(year_dog)
        exit()

    def thirteen():
        print('Program rozmienia podaną kwote na monety.')
        n = input('Podaj kwote:')  # wprowadzenie kwoty jako stringa
        x = n.replace(",", ".")  # zamiana ewentualnego przecinka na kropke
        z = float(x)  # zamiana stringa na floata
        coins_change(z)  # wykonanie funkcji
        exit()

    try:

        odp = int(input('Wpisz cyfre, aby wybrać  program który cię interesuje:'))
        if odp == 0:
            print("Wpisałeś zero! Wpisz liczbę od 1 do 13 ;)")
            value_error()
        elif odp == 1:
            one()
        elif odp == 2:
            two()
        elif odp == 3:
            three()
        elif odp == 4:
            four()
        elif odp == 5:
            five()
        elif odp == 6:
            six()
        elif odp == 7:
            seven()
        elif odp == 8:
            eigth()
        elif odp == 9:
            nine()
        elif odp == 10:
            ten()
        elif odp == 11:
            eleven()
        elif odp == 12:
            twelve()
        elif odp == 13:
            thirteen()
        elif odp >= 14:
            print("Wpisałeś za dużą liczbę! Wpisz liczbę od 1 do 13 ;)")

            value_error()

    except ValueError:
        print('Błąd! Podano nieprawidłowy znak.')
        value_error()


print('Witaj w Multitool Python Program by iSA ')
print('1)Program przelicza liczbę binarną na dziesiętną. \n'
      '2)Program przelicza stopnie Celsjusza na Fahrenheita.\n'
      '3)Program przelicza stopnie Fahrenheita na Celsjusza.\n'
      '4)Program sprawdza czy liczba jest podzielne przez 3,5 oraz 7.\n'
      '5)Program  sprawdza czy liczba jest podzielna przez 3 lub 5 lub 7.\n'
      '6)Program sprawdza czy podana liczba jest liczbą parzystą czy nieparzystą.\n'
      '7)Program wyświetla pierwszą i ostatnią cyfrę w liczbie..\n'
      '8)Program oblicza pole powierzchni koła.\n'
      '9)Program rysuje prostokąt o podanych rozmiarach za pomocą znaków +, - , | .\n'
      '10)Program oblicza czy dany rok jest rokiem przestępnym.\n'
      '11)Program za pomocą znaku # rysuje piramidę.\n'
      '12)Program przelicza wiek psa na wiek człowieka\n'
      '13)Program rozmienia podaną kwote na monety. ')
value_error()
