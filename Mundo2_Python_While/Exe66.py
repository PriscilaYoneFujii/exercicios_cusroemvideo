'''
Crie um programa que leia números inteiros
pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre elas
(desconsiderando o flag)
'''
soma = dig = 0
cont = -1
print('Para sair digite 999')
while True:
    soma += dig
    cont += 1
    dig = int(input('Digite um valor inteiro: '))
    if dig == 999:
        break
print(f'Soma: {soma}\nnúmeros digitados {cont}\nMédia dos números digitados(exceto flag): {(soma/cont):.2f}')