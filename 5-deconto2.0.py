import os
os.system('cls')

#entrada
valor_do_produto = float(input('digite o valor do produto: '))
pagamento = 'digite forma de pagamento 1 or 2: '


#process

desconto = valor_do_produto * 0.10
valor_com_desconto = valor_do_produto - desconto
match pagamento:
    case 1:
        print('10% de esconto')
    case 2:
        print('pode parcelar ate 6 vezes')

print(f'valor com desconto de 10%{valor_com_desconto}')