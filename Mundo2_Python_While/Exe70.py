gasto_total = qtmaior_gasto = cont = menor_gasto= 0
resp = 'S'
#menor_gasto = 99999.99
while True:
    print('-'*30)
    if resp != 'N':
        nome_prod=str(input('Nome do produto: '))
        preco_prod=float(input('Preço do produto: '))
        cont += 1
        gasto_total += preco_prod
        if preco_prod >= 1000:
            qtmaior_gasto += 1
        elif preco_prod < menor_gasto or cont == 1:
            prod_barato = nome_prod
            menor_gasto = preco_prod
        resp = str(input('Deseja continuar o cadastro? [S/N]: ')).upper()
    else:
        break
print(f'total gasto na compra: R${gasto_total:.2f}')
print(f'produtos custam mais de R$1000: {qtmaior_gasto}')
print(f'o produto mais barato é o {prod_barato} de {menor_gasto}')
'''
while True:
   produto=str(input('Nome do produto: ')) 
   preco=float(input('Preco: R$))
   ETC....
   resp = ' '
   while resp not in 'SN':
       resp = str(input('Quer continuar? [S/N]: '))
    if resp == 'N':
        break

!mercado não gosta da gambiarra do "menor preço = 999..."? oxe...
solução:
ETC->
if preco > 1000:
    maisquemil += 1
if cont == 1 or preco < menor:
    menor = preco
    barato = produto
'''