import time
s = ''
v = False
while v != True:
    print('\n')
    s = str(input('Sexo [M / F]: ')).upper()
    if s =='F':
        v = True
        print('acertou miseravi!')
    elif s in 'Mm':
        v = True
        print('acertou miseravi!')
    else:
        print('Errooooou')
        time.sleep(1)


