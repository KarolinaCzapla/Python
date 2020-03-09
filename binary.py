# 6. Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny. Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.
# brak ograniczenia na znaki 0/1
number = int(input("Podaj liczbe: "))
number_a = len(str(number))
if number_a !=6:
    print("Liczba musi zawierać 6 cyfr !")
else:
    x = 0
    y = 0
    while number > 0:
        y += 2 ** x * (number % 10)
        number //= 10
        x += 1
    print(y)