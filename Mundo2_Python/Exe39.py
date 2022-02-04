from datetime import datetime
#datenac=input('profavor digite sua data de dacimento:')
#ano=input('Ano ')
#mes=input('Mês ')
#dia=input('Dia ')
#ano, mes, dia = map(int, datenac.split('-'))
nacimento = datetime.date(1997, 11, 22)
dataHoje = datetime.today()
#nacimentoresult = datetime.datetime.combine(nacimento, datetime.time(0, 0))
result = dataHoje - nacimento
if result < 18:
    print('Ainda não está preparado!')
elif result == 18:
    print('Já pode se alistar meu jovem')
else:
    print('Já passou do seu tempo!')