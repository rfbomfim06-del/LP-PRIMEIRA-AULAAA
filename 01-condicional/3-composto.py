import os
os.system('cls')


idade = int(input('digite sua idade: '))

if idade < 16:
    print('nao podem votar')
elif idade < 18:
    print('voto opcinal')
elif idade <= 65:
    print('voto obrigatorio')
else:
    print('voto obrigatorio')
    



