from datetime import date
anoAtual = date.today().year
anoNacimento = int(input('Ano em que você nasceu: '))
idade = anoAtual - anoNacimento
falta = idade - 18
if idade < 18:
    print('Ainda não está preparado! faltam {} anos para se alistar'.format(18 - idade))
    print('idade', idade)
elif idade == 18:
    print('Já pode se alistar meu jovem')
    print('idade', idade)
elif idade > 18:
    print('Já passou {} anos do seu alistamento'.format(falta))
    print('idade', idade)