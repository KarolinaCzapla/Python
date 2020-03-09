# 7. Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie.
print("Program rozpoznaje czy podana liczba jest liczbą parzystą czy nieparzystą.")
while True:
    x=int(input("Podaj liczbę:"))
    if x % 2 ==0:
        print("Liczba jest parzysta!")
    else:
        print("Liczba jest nieparzysta!")