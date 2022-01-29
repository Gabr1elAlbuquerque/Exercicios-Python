from random import randint
print('Seu carro passou pelo radar.')
vel = randint(10, 180)
if vel > 80:
    print('Seu veículo estava a {}KM/h, {}KM/h acima do máximo permitido'.format(vel, vel - 80))
    print('Por isso, deverá pagar uma multa de R${}'.format((vel - 80) * 7))
else:
    print('Sua velocidade é {} KM/h, você está dentro do limite, continue assim!'.format(vel))
