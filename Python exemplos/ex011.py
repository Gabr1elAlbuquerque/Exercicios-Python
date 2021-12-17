print('\033[1;30m', 'CALCULADORA DE TINTA PARA PAREDE', '\033[m')
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Agora a altura da parede em metros: '))
area = l * a
tinta = area / 2
print('Uma parede de {:.2f}m de largura e {:.2f}m de altura tem a área de {:.2f}m²'.format(l, a, area))
print('Para a área de {:.2f}m², serão necessários {:.2f}L de tinta.'.format(area, tinta))
