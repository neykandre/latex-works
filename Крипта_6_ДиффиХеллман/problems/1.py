from alph import alph

descr = 28

encrypted = [24, 9, 24, 11, 15, 28, 17, 2, 6, 28, 15, 25, 24, 11, 24, 11, 1]

for el in encrypted:
    print(alph[el * descr % 29], end='')