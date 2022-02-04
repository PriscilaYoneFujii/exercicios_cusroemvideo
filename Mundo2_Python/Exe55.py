import os

os.system('cls')
val_peso = float(input('peso da pessoa: '))
m = val_peso
M = val_peso
listin = []
for c in range(0, 3):
    listin.insert(c, val_peso)
    val_peso = float(input('peso da pessoa: '))
    if val_peso > M:
        M = val_peso
    elif val_peso < m :
        m = val_peso

os.system('cls')
print('menor peso: {:.2f}\nmaior peso: {:.2f}'.format(m, M))
print(listin)