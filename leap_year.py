# 10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
print("Program sprawdza czy podany rok jest rokiem przestępnym.")
while True:
    x = int(input("Podaj rok: "))
    if x % 4 == 0:
        print("Rok %d jest rokiem przestępnym " % (x))
    else:
        print("Rok %d nie jest rokiem przestępnym " % (x))