import random

def getYou(opc):
    if opc == "tesoura":
        o = 0
        return o
    elif opc == "pedra":
        o = 1
        return o
    else:
        o = 2
        return o

def getJyanken(qual, o):
    if qual == o:
        print("aiko,\nvocê {}, oponente {}".format(itens[o], itens[qual]))
    elif o < qual < 2:
        print("você perdeu,\nvocê: {}, oponente: {}".format(itens[o], itens[qual]))
    elif qual < o < 2:
        print("você ganhou,\nvocê: {}, oponente: {}".format(itens[o], itens[qual]))
    elif qual < 1 < o:
        print("você perdeu,\nvocê: {}, oponente: {}".format(itens[o], itens[qual]))
    elif 0 < qual < o:
        print("você ganhou,\nvocê: {}, oponente: {}".format(itens[o], itens[qual]))
    elif o < 1 < qual:
        print("você ganhou,\nvocê: {}, oponente: {}".format(itens[o], itens[qual]))
    elif 0 < o < qual:
        print("você perdeu,\nvocê: {}, oponente: {}".format(itens[o], itens[qual]))
    elif qual < 1 < o:
        print("você perdeu,\nvocê: {}, oponente: {}".format(itens[o], itens[qual]))
        
qual = (random.randint(0, 2))

itens = ('pedra', 'papel', 'tesoura')
stt2 = getYou(itens[0])
getJyanken(qual, stt2)