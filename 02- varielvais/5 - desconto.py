import os 

#limpa o terminal
os.system('cls')

print('= solicitando dados =')
valor = float(input('digite o valor'))

#calcule
#desconto
desconto = valor * 0.10
valor_com_desconto = valor - desconto

print('\n= exibindo dados =')
print('valor com desconto de 10%:',valor_com_desconto)
