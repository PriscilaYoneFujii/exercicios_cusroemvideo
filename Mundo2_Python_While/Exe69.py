contMias18 = 0
contaHomem = 0
contMulhermenos20 = 0
resp = str(input('Quer iniciar? ')).upper()
print('='*30)
while True:
    if resp != 'N':
        sexo = str(input('Sexo da pessoa: ')).upper()
        idade = int(input('Idade da pessoa: '))
        print('='*30)
        if sexo in 'Mm':
            contaHomem += 1
        if idade > 18:
            contMias18 += 1
        if idade < 20 and sexo in 'Ff':
                contMulhermenos20 += 1
    else:
        break
    resp = str(input('Quer continuar? ')).upper()

print(f'quantidade de pessoas tem mais de 18 anos {contMias18}')
print(f'quantidade de homens cadastrados {contaHomem}')
print(f'quantidade de mulheres tem menos de 20 anos {contMulhermenos20}')