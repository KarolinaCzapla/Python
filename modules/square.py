# Program rysuje prostokąt o podanych rozmiarach za pomocą znaków +, - , | .

def square():
    try:
        x = int(input('Podaj liczbę wierszy: '))
        y = int(input('Podaj liczbę kolumn: '))
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
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        square()
