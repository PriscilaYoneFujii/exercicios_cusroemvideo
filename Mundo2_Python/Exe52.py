# quais são os números primos
cont = 0
n = int(input('valor: '))
for c in range(1,n):
    if n%c==0:
        cont += 1

if cont > 2:
    print('não é primo, contagem {}'.format(cont))
else:
    print('este é primo! a contagem {}'.format(cont))

