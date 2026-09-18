from operator import not_
import os
os.system('cls')

#entrada 
nome = input('digite seu nome: ')
primeira_nota = int(input('digite sua nota: '))
segunda_nota = int(input('digite sua nota: '))

#processamneto
media = primeira_nota * segunda_nota /2
if media >= 9:
    conseito ='A'
elif media <= 7.5:
    conseito ='B'
    
elif media  <= 6:
    conseito ='C'
    
elif media <= 4:
    conseito ='D'
    
else:
    conseito = 'F'
    

if media >= 6:
    resultado = 'aprovado'
else:
    resultado = 'REPROVADO'


#saida

print('media:',media)
