# progressão aritimética
# {an = a1 + (n - 1)*r} | a1=primeiro termo, n = N de termos existentes até o an, R=razão

a1 = int(input('Qual o primeiro termo: '))
razao = int(input('\nQual a razão da progressão? '))
n = int(input('\nQual termo gostaria de saber? '))

for c in range(a1, 11, razao):
    print('{}'.format(c, end=' ->'))

an = a1 + (n-1)*razao
print('\nE o n gésimo termo é {}'.format(an))
# 2 4 6 8 10 -> N=5, a1=2, r=2 ->
