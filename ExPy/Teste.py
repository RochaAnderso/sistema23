import time
from colorama import Fore
import os
import shutil
print (Fore.YELLOW+'Olá seja bem vindo ao SESC IPARANA')

endereço='Rua Professor José Henrique'
num='365'

nome=input('Antes de comerçarmos nosso atendimento me informe seu nome:')
print(Fore.CYAN+'''Olá {} ,me chamo Júlia e sou atendente virtual do SESC IPARANA,Digite: 
[1] Se você deseja fazer um check-in
[2] Se você deseja fazer uma reserva
[3] Serviços de comorbidade
[4] Informações Locais e atrações turisticas''' .format ((nome)))

opcao=int(input('Digite a opcão que você deseja!'))
if opcao ==1:
    print ('Vi que seu nome é {}, para fazer o check-in precisamos também adicionar a foto do seu RG,faça o upload a seguir '.format ((nome)))
    filergfrente= input('Digite aonde está o arquivo do RG (FRENTE)')
    if filergfrente == 'imgrg\RGFRENTE.jpg':
        print(Fore.GREEN+('UPLOAD FEITO COM SUCESSO'))
        filergcosta= input('Digite aonde está o arquivo do RG (COSTA)')
        if filergcosta == 'imgrg\RG COSTA.jpg':
            print(Fore.GREEN+('UPLOAD FEITO COM SUCESSO'))

    else:
        print(Fore.RED+('UPLOAD NEGADO'))
else:
    print(Fore.RED+'Opção invalida')

