import os

#limpa o terminal.
os.system('cls')

print('= solicitando dados =')
nome = input('digite seu nome:')
idade = int(input('digite sua idade'))
primeira_nota = float(input('digite a primeira nota:'))
segunda_nota = float(input('digite a segunda nota:'))


media = (primeira_nota + segunda_nota) /2 

print('\n= exibindo dados =')
print('nome:', nome)
print('idade:', idade)
print('primeira_nota:', primeira_nota)
print('segunda_nota:', segunda_nota)
print('media:',media)
