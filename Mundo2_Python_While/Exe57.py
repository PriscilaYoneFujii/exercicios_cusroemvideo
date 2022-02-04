#introdução ao While
#- comparando com for, o while é usado para atingir
#   uma meta não padrão, ou seja, que depende de uma str
#   uma condição, um booleano, etc.
#   o for roda dentro do limite que vc estabelece, mas o
#   while tem mais opções.
import time
import os
import random
n=0
acerto = False
tente = 0
valor_oculto = random.randint(0, 100)
print('olá, escolhi um número entre 0 e 100, tente advinhar\nentão vamos lá!')
time.sleep(5)
while acerto!=True:
    os.system('cls')
    z = int(input('tente acertar o valor: '))
    if z < valor_oculto:
        print('\nErrado.. o valor é MAIOR')
        tente +=1
        time.sleep(2)
    elif z > valor_oculto:
        print('\nErrado.. o valor é menor')
        tente +=1
        time.sleep(2)
    else:
        acerto = True
print('Parabéns, você acertou com {} tentativas'.format(tente))


