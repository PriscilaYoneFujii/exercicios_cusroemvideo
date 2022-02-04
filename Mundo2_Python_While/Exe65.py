import os
med = soma = cont = maior = 0
r='S'
menor = 9999
while r != 'N':
    num = int(input('Digite qualquer valor inteiro: '))
    soma += num
    cont += 1
    if num < menor:
        menor = num
    elif num > maior:
        maior = num
    r = str(input('Deseja continuar? [S/N]: ')).upper()
#os.system('cls')
print('\nA média dos números: {:.1f}\nQuantidade de números: {}'.format(soma/cont, cont))
print('O maior número foi {} e o menor número foi {}'.format(maior, menor))