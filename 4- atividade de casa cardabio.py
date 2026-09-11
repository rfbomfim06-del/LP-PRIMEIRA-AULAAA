import os
os.system('cls')
#entrada
codigo = int(input('digite o codigo : '))

#processo
print("===== CARDÁPIO =====")
print("1 - Picanha       R$ 25,00")
print("2 - Lasanha       R$ 20,00")
print("3 - Strogonoff    R$ 18,00")
print("4 - Bife Acebolado R$ 15,00")
print("5 - Pão com ovo   R$ 5,00")

match codigo:

    case 1:
        prato = "Picanha"
        valor = 25.00

    case 2:
        prato = "Lasanha"
        valor = 20.00

    case 3:
        prato = "Strogonoff"
        valor = 18.00

    case 4:
        prato = "Bife Acebolado"
        valor = 15.00

    case 5:
        prato = "Pão com ovo"
        valor = 5.00

    case _:
        prato = "Código inválido"
        valor = 0

#saida
print("\nPrato escolhido:", prato)
print("Valor: R$", format(valor, ".2f")) 