tab = int(input('Digite o número da tabuada: '))
while True:
    if tab >= 0:
        aux = 0
        while aux <= 10:
            print(f'{tab} X {aux} = {tab*aux}')
            aux += 1
        print('='*30)
    else:
        print('Terminado.')
        break
    tab = int(input('Qual número da tabuada?\nPara sair digite um número negativo'))

    '''
Dentro do While True do Prof:
    n = int(input('Qualquer valor: '))
    if n<0:
        break
    print('-'*30)
    for c in range(0, 11):
        print(f'{tab}X{aux}={tab*aux}')
    print('-'*30)
print('Programa terminado, volte sempre!')
    '''