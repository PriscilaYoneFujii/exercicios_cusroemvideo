#Exercício Python 44: Elabore um programa que calcule o valor a ser pago
#por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
#   (valor * val_descPerc = 10)/100
# – à vista no cartão: 5% de desconto
#   (valor * val_descPerc = 5)/100
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros
#   valor+(valor * (val_descPerc = 20)/100)
import os
string_S = "%"
result = 0
def getOpc(opc, valor):
    os.system('cls')
    if opc == 1:
        result = valor-((valor * 10) / 100)
        print("valor avista fica com 10{}, e o desconto é : {}".format(string_S, result))
    elif opc == 2:
        result = valor-((valor * 5) / 100)
        print("valor no cartão fica com 5{}, e o desconto é : {}".format(string_S, result))
    elif opc == 3:
        result = valor
        print("esta opção de pagamento não possui desconto. O valor será: {}".format(result))
    else:
        result = valor + (valor * 20)/100
        print("esta opção de pagamento acrescenta 20{} de Juros sobre o valor de pagamento, totalozando em: {}.".format(string_S, result))


print("por favor, qual a opção de pagamento e o valor da compra?")
valor = int(input('valor da compra:'))
print("quanto as opções de pagamento:\n",
"1 - pagamento a vista;\n",
"2 - pagamento a vista no cartão\n",
"3 - pagamento em até 2X no cartão\n",
"4 - pagamento em 10X no cartão ou 10X no carnê \n")
opc = int(input())
getOpc(opc, valor)
