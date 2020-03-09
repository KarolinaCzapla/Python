
# # 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
print("Program  sprawdza czy liczba jest podzielna przez 3 lub 5 lub 7")
while True:
    x=int(input("Podaj liczbę: "))
    if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        print("Liczba jest podzielna!")
    else:
        print("Liczba nie jest podzielna!")