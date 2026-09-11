import os
os.system('cls')

#entrada
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))
sexo = input("Digite o sexo (M para Masculino ou F para Feminino): ").strip().upper()
#processo
match sexo:
    case 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    case 'F':
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
    case _:
         print("Opção de sexo inválida! Digite apenas M ou F.")

#saida





