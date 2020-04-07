# Program za pomocą znaku # rysuje piramidę.



def pyramid():
    try:
        width = int(input('Podaj wysokość piramidy: '))
        for i in range(0, width):
            for j in range(0, width - i):
                print(" ", end="")
            for k in range(0, 2 * i + 1):
                print("#", end="")
            print("")
    except ValueError:
        print("Podano nieprawidłowe dane! Podaj cyfrę!")
        pyramid()
