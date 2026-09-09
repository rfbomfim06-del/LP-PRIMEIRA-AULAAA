import os
os.system('cls')

#entrada
dia = input('digite o dia da semana:').lower()

#processo
match dia:
    case 'segunda':
        print('hoje é segunda-feira.')
    case 'terça':
        print('hoje é terça-feira.')
    case 'quarta':
        print('hoje é quarta-feira.')
    case 'quinta':
        print('hoje é quinta-feira.')
    case 'sexta':
        print('hoje é sexta-feira.')
    case 'sábado'| 'domingo':
        print('hoje é final de semana.')
    case _:
        print('dia invalido.')

print(dia)

