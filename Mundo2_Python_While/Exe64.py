#dentro de um loop while, continue lendo os números até digitar 999(flag)
# no final do loop, imprima a soma dos números digitados e a quantidade de
# números digitados
soma= dig = 0
cont = -1
while dig != 999:
    soma += dig
    cont += 1
    dig = int(input('Digite um valor inteiro: '))
print('Soma: {}\n{} números contados'.format(soma, cont))