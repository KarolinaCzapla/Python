def statistics():
    import openpyxl

    filename = 'text.txt'

    num_line = 0
    num_words = 0
    num_chars = 0  # ze spacjami
    num_upp = 0
    num_low = 0
    file = open(filename, 'r+')
    for x in file:
        word_list = x.split()
        num_line += 1
        num_words += len(word_list)
        num_chars += len(x)

    print(f'Liczba linii: {num_line}\nZnalezionych wyrazów: {num_words}'
          f'\nPrzeanalizowanych znaków(razem ze spacjami): {num_chars}')

    file = open(filename, 'r+')
    read_file = file.read()
    for c in read_file:
        if c.isupper():
            num_upp += 1
        elif c.islower():
            num_low += 1
    sum_chars = num_low + num_upp  # bez spacji
    print(f'Przeanalizowanych znaków(bez spacji):{sum_chars}'
          f'\nIlosc malych liter: {num_low}'
          f'\nIlosc wielkich liter: {num_upp}')

    excel = openpyxl.Workbook()
    excel.save("stat_text.xlsx")
    nazwa_pliku = "stat_text.xlsx"
    excel = openpyxl.load_workbook(nazwa_pliku)
    arkusz = excel.active
    rows = [('Liczba lini', 'Znalezionych wyrazów',
             'Ilosc malych liter', 'Ilosc wielkich liter',
             'Znaki ze spacja', 'Znaki bez spacji'),
            (num_line, num_words, num_low, num_upp, num_chars, sum_chars)
            ]
    for row in rows:
        arkusz.append(row)

    excel.save(nazwa_pliku)


statistics()
