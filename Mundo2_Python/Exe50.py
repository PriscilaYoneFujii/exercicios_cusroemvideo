# leia qualquer número, mas some somente os que forem par
cont = 0
sumu = 0
for c in range(1, 7):
    num = int(input('digite um número:'))
    if (num%2==0):
        cont += 1
        sumu += num

print('asomatoria é {}, e a quantidade de pares encontrados são: {}'.format(sumu, cont))