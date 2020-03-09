# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
print("Program oblicza pole powierzchni koła o podanym promieniu.\nPole obliczane jest za pomocą wzoru:Pole = ((promien ** 2) * 3.14)")
while True:
    radius = float(input('Podaj dlugość promienia: '))
    area = ((radius ** 2) * 3.14)
    print("Pole wynosi %.2f " %(area))
