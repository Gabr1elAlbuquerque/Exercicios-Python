print('\033[1;30m', '=' * 10, 'CONVERSOR DE MOEDAS', '=' * 10, '\033[m')
n = float(input('Digite a quantidade para ser convertida R$:'))
dol = n / 5.60
pounds = n / 7.44
print('Com R${:.2f} você pode trocar por U$${:.2f} ou £{:.2f}.'.format(n, dol, pounds))
