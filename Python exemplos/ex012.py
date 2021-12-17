produto = float(input('Digite o valor do produto R$: '))
novo = produto - (produto * 5 / 100)
print('Um produto que custava R$:{:.2f} custará, com o desconto de 5%, R$:{:.2f}'.format(produto, novo))

