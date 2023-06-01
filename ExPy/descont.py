from colorama import Fore
preço= float(input('Digite o preço da mercadoria em R$:'))
percentual= float (input('Digite o percentual de desconto:'))
desconto = (percentual/100) * preço
preçofinal= preço-desconto
print('O valor do desconto é {} e o produto com valor final é {}'.format(desconto,preçofinal))
