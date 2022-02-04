# faça uma lista contendo o ano de nascimento de 7 pessoas
# e informa quantas delas ainda não são maiores de idade
import datetime

hoje = datetime.date.today()
esseano = int(hoje.strftime("%Y"))
maioridade = 0
menoridade = 0
aux = []
listin = []
for c in range(0, 3):
    listin.insert(c, int(input('Ano de nascimento: ')))
    if (esseano-listin[c])>=18:
        maioridade += 1
    else:
        menoridade += 1

print('Dos usuários informados,\n{} são de maior idade,\ne {} são de menor idade.'.format(maioridade, menoridade))
print('A lista:\n',listin)
# solução do prof:
#from datatime import date
#ano = date.today().year
# o resto é quase igual