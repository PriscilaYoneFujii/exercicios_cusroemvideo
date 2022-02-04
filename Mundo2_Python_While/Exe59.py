'''leia dois números e forneça as opções entre:
    somar; multiplicar; Maior; novos números;
    sair do programa;
'''
import os
import time
def fazSoma(n,m):
    return n+m
def fazMultplicar(n,m):
    return n*m
def qualMaior(n,m):
    if n > m:
        print('Maior {}'.format(n))
    elif m > n:
        print('Maior {}'.format(m))
    else:
        print('os dois são iguais')
def newNumbers(n, m):
    n = int(input('valor para n: '))
    m = int(input('valor para m: '))
    os.system('cls')
    return n, m
def getMenssage():
    print('[1] : Somar os números\n[2] : Multiplicar os números',
    '\n[3] : Eleger qual é o maior\n[4] : Alterar os valores de n e m\n[5] : sair do programa...')
# principal

print('A seguir favor informe dois números e escolha a opção de operação\n')
m = int(input('valor de m: '))
n = int(input('valor de n: '))
result = 0
os.system('cls')
getMenssage()
resp = int(input('_: '))
while resp != 5:
    if resp >= 6:
        print('opção inválida tente novamente..')
        time.sleep(2)
    elif resp == 4:
        n, m = newNumbers(n, m)
        print('novos valores, n={} e m={}'.format(n,m))
        time.sleep(5)
    elif resp == 3:
        qualMaior(n, m)
        time.sleep(5)
    elif resp == 2:
        result = fazMultplicar(n,m)
        print('resultado: {}'.format(result))
        time.sleep(5)
    else:
        result = fazSoma(n,m)
        print(result)
        time.sleep(5)
    os.system('cls')
    getMenssage()
    resp = int(input('_: '))