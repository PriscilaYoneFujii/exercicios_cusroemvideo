import os
import time
k=n=m=0
def numero_Termos(k):
    k = int(input('Quantos termor deseja imprimir? '))
    return k

def novo_ValorPA(n,m,k):
    n = int(input('Novo primeiro termo: '))
    m = int(input('Nova razão da progressão: '))
    k = numero_Termos(k)
    return n, m, k

def getErrorMenssage():
    print('O valor inserido não é valido!\nTente novamente!')

def endOption():
    resp = input('\nDeseja continuar?\n[ S / N ]: ').upper()
    if resp != 'N':
        return True
    else:
        return False

def alterar_valor(n, m, k):
    print('Desera alterar algum valor?')
    resp = input('[ S / N ]: ').upper()
    return resp

a1 = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão da progressão? '))
termo = a1
aux = 1
o = True
#'''
k = numero_Termos(k)
while o != False:
    resp = alterar_valor()
    if resp == 'N':
        while aux <= k:
            print('{}'.format(termo),end=' -> ')
            termo += razao
            aux += 1
    else:
        a1, razao, k = novo_ValorPA(a1, razao, k)
    print(' fim da PA')   
    time.sleep(4)
    os.system('cls')
    o=endOption()
    
print('* fim do programa *')