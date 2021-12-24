from random import shuffle, choice
print('O programa escolherá a pessoa para executar determinada ação.')
p1 = str(input('Primeira pessoa: ')).strip()
p2 = str(input('Segunda: ')).strip()
p3 = str(input('Terceira: ')).strip()
p4 = str(input('Quarta: ')).strip()
lista = [p1, p2, p3, p4]
escolhido = choice(lista)
print('O(a) escolhido(a) foi {}{}{}.'.format('\033[1;31m', escolhido, '\033[m'))
