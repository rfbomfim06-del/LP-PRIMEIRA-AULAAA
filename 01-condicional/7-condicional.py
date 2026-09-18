import os

os.system('cls')

#entrada
nota = int(input('nota:'))
primeira_nota = int(input('digite o primeira nota: '))
segunda_nota = int(input('digite o segunda nota: '))
terceira_nota = int(input('digite o tercira nota: '))
#processamento.
media = (primeira_nota + segunda_nota + terceira_nota) / 3
if nota >= 7:
    print('aprovado')
else:
    print('reprovado')


#saida.
print('primerira_nota:',primeira_nota)
print('segunda_nota:',segunda_nota)
print('tercira_nota:',terceira_nota)
print('media:',media)
