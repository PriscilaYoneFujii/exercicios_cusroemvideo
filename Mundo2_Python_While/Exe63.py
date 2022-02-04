# leia um valor que será o número de termos da sequência de fibonnaci
# fibo = val + valantrior
# 0 + 1 = 1 -> 1 + 1 = 2 -> 1 + 2 = 3 -> 2 + 3 = 5 -> 3 + 5 = 8 ...
p1 = 1
p2 = 0
aux = 0
cont = int(input('Quantos termos quer imprimir? '))
print('{} -> {}'.format(aux, p1),end='')
while cont > 0:
    aux = p1+p2
    print(' -> {}'.format(aux),end='')
    p2 = p1
    p1 = aux
    cont = cont - 1
print(' END')
'''
t1 = 0
t2 = 1

'''