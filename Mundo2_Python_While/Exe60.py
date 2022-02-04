#leia e calcule o fatorial do interio
import os
resp = ''
while resp != 'e':
    n = var = int(input('Digite um valor: '))
    aux = var
    while aux != 1:
        var *= aux-1
        aux -= 1
    print('fatorial de {}! é: {}'.format(n, var))
    print('\nDeseja continuar?\nNão: e\nSim: qualquer tecla')
    resp = str(input('_'))
    os.system('cls')
'''
O professor usou um módulo fatorial da biblioteca math
EX:
from math import factorial
n = int(input())
f = factoriar(n)
tá fácil desse jeito
'''
#-----------------------------------------------------------------------
'''
val = int(input())
aux = 0
for c in range(1, val+1):
    aux *= c+1
print(aux)
'''