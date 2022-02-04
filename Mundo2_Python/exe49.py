# tabuada v2.0 - com laço for
def tabuada(n):
    for c in range(1, 11):
        r = c*n
        print('{} X {} = {}'.format(c, n, r))

num = int(input('de qual número quer saber a tabuada?\n'))

tabuada(num)