import os
os.system('cls')

#entrada 
usuario = input ('digite seu nome: ')
faltas = int(input('digite sua falta: '))
media = float(input('digite sua media:'))
#processos
if media <= 7 and  faltas <= 40:
    print('aprovado')
else:
    print('reprovado')