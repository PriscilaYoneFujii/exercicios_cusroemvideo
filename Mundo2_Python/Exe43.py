#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice
#de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – Abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
# -> exemplo: IMC = Peso ÷ (Altura × Altura), Altura em m.


peso = float(input("seu peso: "))
altura = float(input("sua altura: "))

def qualIMC(p, a):
    imc = p / (a * a)
    if imc < 18.5:
        print("O imc é {:.1f}".format(imc),"\nMagreza absoluta '_' ")
    elif 18.5 <= imc < 25:
        print("O imc é {:.1f}".format(imc),"\npeso ideal ^_^")
    elif 25 <= imc < 30:
        print("O imc é {:.1f}".format(imc),"\nsobrepeso, olha láh *_*")
    elif 30 <= imc < 40:
        print("O imc é {:.1f}".format(imc),"\nTá obeso... \-_-/")
    else:
        print("O imc é {:.1f}".format(imc),"\nobesidade Mórbida, MDS *O*")

qualIMC(peso, altura)