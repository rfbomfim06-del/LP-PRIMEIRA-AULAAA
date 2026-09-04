import os
os.system('cls')

#entrada
nota = int(input('digite uma nota: '))

#processo
if nota >= 0 and nota <= 10:
    print(f'{nota}')
else:
    print(f'{nota}: deve esta entre 0 e 10')