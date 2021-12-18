from math import trunc
numero = float(input('Digite um número decimal para ver sua parte inteira: '))
inteiro = trunc(numero)
print('O número {} tem sua parte inteira igual a {}.'.format(numero, inteiro))
