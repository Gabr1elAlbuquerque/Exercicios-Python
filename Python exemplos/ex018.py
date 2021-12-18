from math import radians, sin, cos, tan
angulo = int(input('Digite um ângulo para ver seu seno, cosseno e tangente: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('{}° tem o seno valendo {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))
