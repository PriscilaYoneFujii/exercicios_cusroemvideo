#faça um jogo de par ou impar com o computador
from random import randint
cont = 0
you = int(input('Digite um valor inteiro: '))
while True:
    comp = randint(0, 50)
    imppr = str(input('Você quer par ou impar? [P/I]: ')).upper()
    if imppr == 'P':
        if (you + comp) % 2 == 0:
            print('Voce GANHOOOOU!\nParabens')
            print(f'Você: {you}  Computador: {comp}  Soma: {you+comp}')
            cont += 1
        else:
            print('Você PERDEU...\ntente novamente..')
            print(f'Você: {you}  Computador: {comp}  Soma: {you+comp}')
            print('='*30)
            break
    else:
        if (you + comp) % 2 == 1:
            print('Voce GANHOOOOU!\nParabens')
            print(f'Você: {you}  Computador: {comp}  Soma: {you+comp}')
            cont += 1
        else:
            print('Você PERDEU...\ntente novamente..')
            print(f'Você: {you}  Computador: {comp}  Soma: {you+comp}')
            print('='*30)
            break
    print('='*30)
    you = int(input('Digite um valor inteiro: '))
print(f'Seu total de vitórias: {cont}')