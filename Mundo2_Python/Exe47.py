
def iterandor(num):
    for c in range(1, num+1):
        if (c % 2) == 0:
            print(c," é par")

def aprimorator(num):
    for c in range(2, num+1, 2):
        print(c)

#contagem = int(input('digite qualquer valor numérico: '))
#iterandor(contagem)
#---------- faz a mesma coisa -----------
countt = int(input('digite um valor: '))
aprimorator(countt)