from alph import alph

encrypted = [6, 24, 20, 25, 21, 1]
for descr in range(2, 29):
    print(descr, end=': ')
    for el in encrypted:
        print(alph[el * descr % 29], end='')
    print()
