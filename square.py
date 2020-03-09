# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
while True:
    print("Program rysuje prostokąt o zadanych rozmiarach za pomocą znaków +, - , | ")
    x = int(input("Podaj liczbę wierszy: "))
    y = int(input("Podaj liczbę kolumn: "))
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if (i == 1 or i == x):
                if (j == 1 or j == y):
                    print("+", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("|", end=" ")
        print()
