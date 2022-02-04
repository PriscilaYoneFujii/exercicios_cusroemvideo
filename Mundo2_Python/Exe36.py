#caso If seja falso então será elif quem terá a próxima palavra
#em python, o else é opcional

#calculando porcentagem do salario:
prestacaopossivel = 0
salario = float(input('seu salario: '))
prestacaopossivel = salario - (salario*0.30)
valor_imobiliário = float(input('qual o valor da casa? '))
anual = int(input('em quantos anos pretende pagar? '))
mensalidade = valor_imobiliário/(12*anual)
if mensalidade > prestacaopossivel :
    print("não é possivel fazer este financiamento!")
else:
    print("a mensalidade é possivel, será: R$ %.2f "%mensalidade," por ", anual," anos.")
#se prestação(valorcasa/meses_ano) > 30%doSalario:
#Então emprestimo negado
#Senão emprestimo aceito


#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a
#compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos
#ele vai pagar. A prestação mensal não pode exceder
#30% do salário ou então o empréstimo será negado