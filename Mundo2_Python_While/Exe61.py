a1 = int(input('Qual o primeiro termo: '))
razao = int(input('\nQual a razão da progressão? '))
termo = a1
aux = 1
#'''
while aux <= 10:
    print('{} '.format(termo),end='->')
    termo += razao
    aux += 1
print('fim')

#'''