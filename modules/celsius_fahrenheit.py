# Program przelicza stopnie Celsjusza na Fahrenheita.
def celsius_fahrenheit():
    try:
        celsius = float(input('Podaj temperaturę w stopniach Celsjusza: '))
        fahrenheit = int(((celsius * 9 / 5) + 32))
        print(f'{celsius} ° Celsjusza to {fahrenheit} ° Fahrenheita.')
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        celsius_fahrenheit()


