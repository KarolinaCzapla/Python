# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
print("Program przelicza stopnie Celsjusza na Fahrenheita.\nUżywa do tego wzoru Fahrenheit=((Celsius*9/5)+32.")
while True:
    celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
    fahrenheit = ((celsius*9/5)+32)
    print("%.2f stopni Celsjusza to %.2f stopni Fahrenheita" % (celsius, fahrenheit))