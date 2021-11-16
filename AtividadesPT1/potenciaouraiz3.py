import math
a = float(input('Digite um número:'))
if a>0:
    print('a raiz desse número é: ', end='')
    print(math.sqrt(a))
else:
    print('a potência desse número é:', end='')
    print(a*a)
