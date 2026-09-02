import os
os.system('cls')

#entrada
print('= exibindo dados =')
peso = float(input('digite seu peso: '))
altura= float(input('digite sua altura: '))

#procesasmento 
calculo = peso/ (altura * altura)

if calculo < 18.5:
    conseito = 'ABAIXO DO PESO'
elif calculo <= 18.6 or 24.9 :
    conseito ='PESO IDEAL(PARABENS)'
elif calculo <= 25.0 or 29.9:
    conseito ='levemente acima do peso'
elif calculo <= 30.0 or 34.9:
    conseito ='obesidade grau 1'
elif calculo <= 35.0 or 39.9:
    conseito ='obesidade grau 2(severa)'
elif calculo <=  40:
    conseito ='obesidade grau 3(morbida)'




#saida
print('\n= exibindo dados =')
print(f'calculo: {calculo}')
print(f'conseito: {conseito}')