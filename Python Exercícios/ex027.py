nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Seu primeiro nome é {}.'.format(separa[0]))
print('Seu ultimo nome é {}.'.format(separa[-1]))
