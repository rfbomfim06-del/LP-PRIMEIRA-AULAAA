import os
os.system('cls')
#entrada
matricula = int(input('digite o numero da sua matricula: '))
ano_de_trabalho = int(input('digite o ano que vc comecou na empresa: '))
ano_de_nascimento = int(input('digite o ano que vc nasceu: '))

#processos
if ano_de_trabalho >= 30 or ano_de_trabalho <= 1961:
    aponsentadoria ='REQUERER APONSENTADORIA'
else:
    aponsentadoria ='NAO REQUERER'

#saida

print(f'aponsentadoria:{aponsentadoria}')
