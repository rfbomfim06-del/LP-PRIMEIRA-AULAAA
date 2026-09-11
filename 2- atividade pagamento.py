# Exercício 5
import os
os.system('cls')
valor = float(input("Digite o valor do produto: R$ "))

pagamento = int(input(
    "Digite a forma de pagamento:\n"
    "1 - À vista\n"
    "2 - A prazo\n"
    "Escolha: "
))

match pagamento:

    case 1:
        desconto = valor * 0.10
        total = valor - desconto

        print("\nValor do produto: R$", format(valor, ".2f"))
        print("Forma de pagamento: à vista")
        print("Valor do desconto: R$", format(desconto, ".2f"))
        print("Total a pagar: R$", format(total, ".2f"))

    case 2:
        parcelas = int(input("Digite a quantidade de parcelas (até 6): "))

        if parcelas >= 1 and parcelas <= 6:
            valor_parcela = valor / parcelas

            print("\nValor do produto: R$", format(valor, ".2f"))
            print("Forma de pagamento: a prazo")
            print("Quantidade de parcelas:", parcelas)
            print("Valor por parcela: R$", format(valor_parcela, ".2f"))
            print("Total a prazo: R$", format(valor, ".2f"))

        else:
            print("Quantidade de parcelas inválida. Escolha de 1 a 6.")

    case _:
        print("Forma de pagamento inválida.")