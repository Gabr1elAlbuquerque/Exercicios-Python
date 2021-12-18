print('\033[1;31m', 'Aluguel de Carro', '\033[m')
dia = int(input('Quantos dias você ficou com o carro? '))
km = int(input('Quilômetros rodados: '))
conta = dia * 60 + km * 0.15
print('A conta é R$:{:.2f}'.format(conta))

