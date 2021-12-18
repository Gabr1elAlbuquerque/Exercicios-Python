print('\033[1;30m', '=' * 10, 'Conversor de temperatura', '=' * 10 ,'\033[m')
temp = int(input('Digite a temperatura em grau celsius: '))
tf = temp * 1.8 + 32
tk = temp + 273
print('{}°C equivale(m) a {} fahrenreit e {} kelvin.'.format(temp, tf, tk))
