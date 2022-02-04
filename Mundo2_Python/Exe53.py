#Digite uma frase palíndromo e vereifique se é verdade nou não
import os
fraze = str(input('digite mu palíndromo: '))
faze = fraze.replace(" ", "")
contra = faze[::-1]

if faze != contra:
    os.system('cls')
    print('{} não é palíndromo.\nSem espaço {},\nao contrário {}'.format(fraze, faze, contra))
else:
    os.system('cls')
    print('Tudo certo, a frase {} é palíndromo:\na frase: {}\ncontrário: {}'.format(fraze, faze, contra))


# O jeito do professor, usando o método strip e Upper
# frase = str(input('Frase: ')).strip().upper()
# palavras = frase.split() #Cria um tipo de array de String ['',''..]
# misto = ''.join(palavras) #Une todos os índice em uma string só
# usando o for pra resolver a parada!
# inverso = ''
# for letra in range(len(misto)-1, -1, -1):
#     inverso += misto[letra]
# print(misto, inverso)
# ... compara misto e inverso com if, o resto é igual