verm = '\033[1;31m'
norm = '\033[m'
azul = '\033[1;34m'
preto = '\033[1;30m'
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'.format(verm, n1, norm, azul, n2, norm, preto, s, norm))
