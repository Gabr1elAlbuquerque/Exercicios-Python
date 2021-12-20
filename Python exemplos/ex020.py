from random import shuffle
print('Este programa criará uma ordem de apresentação.')
p1 = str(input('Primeiro(a) apresentador(a): ')).strip()
p2 = str(input('Segundo(a): ')).strip()
p3 = str(input('Terceiro(a): ')).strip()
p4 = str(input('Quarto(a): ')).strip()
lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem de apresentação será {}.'.format(lista))
