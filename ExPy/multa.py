from colorama import Fore
velocidade=float(input('Digite a velocidade do carro'))
if velocidade> 80:
    valordamulta=(velocidade-80)*5
    print (Fore.RED+'VOCE FOI MULTADO , o valor da multa é R${} '.format ((valordamulta)))
if velocidade <=80:
    print(Fore.GREEN+'BOA VIAGEM')