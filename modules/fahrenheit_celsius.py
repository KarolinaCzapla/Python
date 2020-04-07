# Program przelicza stopnie Fahrenheita na Celsjusza.

def fahrenheit_celsius():
    try:
        fahrenheit = float(input('Podaj temperaturę w stopniach Fahrenheita: '))
        celsius = int((fahrenheit - 32.0) * 5 / 9)
        print(f'{fahrenheit} ° Fahrenheita to {celsius} ° Celsjusza')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        fahrenheit_celsius()
