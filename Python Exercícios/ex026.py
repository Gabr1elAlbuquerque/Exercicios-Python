frase = str(input('Digite uma frase: ')).strip()
print('A letra a apareceu {} vez(es) na frase.'.format(frase.count('a')))
print('A primeira letra a apareceu na posição {}.'.format(frase.find('a') + 1))
print('A ultima letra a apareceu na posição {}.'.format(frase.rfind('a') + 1))

