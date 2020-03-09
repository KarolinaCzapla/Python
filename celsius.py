# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
print("Program przelicza stopnie Fahrenheita na Celsjusza.\nUżywa do tego wzoru Celsius = (Fahrenheit – 32) * 5/9.")
while True:
    fahrenheit = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
    celsius = (fahrenheit - 32.0) * 5/9
    print("%.2f stopni Fahrenheita to %.2f stopni Celsjusza"% (fahrenheit, celsius))