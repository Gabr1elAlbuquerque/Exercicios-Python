from random import randint
vermelho = '\033[1;31m'
normal = '\033[m'
verde = '\033[1;32m'
print('=-' * 20)
computador = randint(0, 5)
jogador = int(input('Escolha um número de 0 a 5: '))
if computador == jogador:
    print('Você ganhou, o computador também escolheu {}{}{}.'.format(verde, computador, normal))
else:
    print('Você perdeu, o computador escolheu {}{}{}.'.format(vermelho, computador, normal))
print('=-' * 20)
