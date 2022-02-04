#soma dos imparae múltiplos de três
def somaTresc(num):
    soma = 0
    for c in range(3, (num+1), 3):
        if c % 3 == 0:
            print(c, end=None)
            soma += c
    return soma

it = int(input('valor: '))

val = somaTresc(it)
print(val)
