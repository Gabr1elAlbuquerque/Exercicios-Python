from math import hypot
print('Calculadora de hipotenusa')
cateto1 = float(input('Digite o primeiro cateto: '))
cateto2 = float(input('Segundo cateto: '))
hipotenusa = hypot(cateto1, cateto2)
print('Um triangulo de lados {:.1f} e {:.1f} tem a hipotenusa valendo {:.1f}'.format(cateto1, cateto2, hipotenusa))
#hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1 / 2)# forma matemática


