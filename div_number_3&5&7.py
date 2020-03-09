# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
print("Program sprawdza czy liczba jest podzielne przez 3 i 5 i 7")
while True:
    x = int(input("Podaj liczbę: "))
    if x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
        print("Liczba jest podzielna!")
    else:
        print("Liczba nie jest podzielna!")