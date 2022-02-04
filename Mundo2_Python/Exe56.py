# ler nome idade e sexo de 4 pessoas
# mazer a média da idade
#printar o nome do homem mais velho
#printar quantas mulheres nonere de 20 anos existem dentre os quatro
import os
import time
med = 0
idade = 0
velho = 0
velho_nome = ''
qtFem = 0
print('pro favor informe seu nome, idade e sexo( M | F):')
time.sleep(5)
os.system('cls')
for c in range(0, 3):
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str(input('sexo M | F: ')).upper()
    med += idade
    if idade > velho and sexo == 'M':
        velho = idade
        velho_nome = nome
    elif sexo == 'F' and idade < 20:
        qtFem += 1
    os.system('cls')

med = med / 4
if velho_nome == None or velho_nome == '':
    print('média das idades: {:.1f}'.format(med),
    '\nnão tem homem nesta lista !',
    '\nquantidade de mulheres com menos de 20 anos é: {}'.format(qtFem))
elif qtFem == None or qtFem == 0:
    print('média das idades: {:.1f}'.format(med),
    '\no homem mais velho da lista: {}'.format(velho_nome),
    'não tem mulher nesta lista !')
else:
    print('média das idades: {:.1f}'.format(med),
    '\nhomem mais velho da lista: {}'.format(velho_nome),
    '\nquantidade de mulheres com menos de 20 anos é: {}'.format(qtFem))
