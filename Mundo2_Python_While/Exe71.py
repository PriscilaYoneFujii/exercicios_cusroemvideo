#saldo = 70000
cont50 = cont10 = cont20 = cont1 = 0
resp = 'S'
while True:
    if resp not in 'NS':
        resp = str(input('S para continuar.\nN para encerrar. _: ')).upper()
    elif resp == 'N':
        break
    else:
        saque = int(input('Quanto deseja sacar? R$'))
        total = saque
        while total >=50:
            cont50 += 1
            total -= 50
        while total >= 20:
            cont20 += 1
            total -= 20
        while total >= 10:
            cont10 += 1
            total -= 10
        while total >= 1:
            cont1 += 1
            total -= 1
    print(f'{cont50} notas de 50R$\n{cont10} notas de 10R$\n{cont20} notas de 5R$\n{cont1} notas de 1R$')
    resp = str(input('S para continuar.\nN para encerrar. _: ')).upper()