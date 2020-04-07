# Program rozmienia podaną kwote na monety.
def coins_change():
    n = input('Podaj kwote:')# wprowadzenie kwoty jako stringa
    x = n.replace(",", ".")# zamiana ewentualnego przecinka na kropke
    z = float(x)# zamiana stringa na floata
    coins = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    coins_a = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    i = 0
    z = round(z * 100)
    coins_len = len(coins)
    while z > 0:
        if coins_a[i] > z:
            if i < coins_len:
                i = i + 1
        else:
            z = (z - coins_a[i])
            print(coins[i], end=" PLN    ")


