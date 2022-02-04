print('olá, bem-vindo ao conversors de números!')
opc = 'sim'
opc_conv = 0
nc = 0
while opc=='sim':
    num = int(input('Digite um inteiro: '))
    opc_conv = int(input('opção de converção 1-binário, 2-octal, 3-hexadecimal: '))
    if opc_conv == 1:
        print(bin(num))
        nc = bin(num)
        print(type(nc))
    elif opc_conv == 2:
        print(oct(num))
        nc = oct(num)
        print(type(nc))
    elif opc_conv == 3:
        print(hex(num))
        nc = hex(num)
        print(type(nc))
    
    opc = input('deseja continuar? sim / nao:  ')

