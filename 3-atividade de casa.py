import os
os.system('cls')
#entrada
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))

#processo
operador = (input(''' 
escolha a operador\n 
+\n
-\n
*\n
/\n
'''))

match operador:
    case  '+':
        resultado = num1 +  num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        resultado = num1 / num2
    case _:
        resultado = 'operador invalido'


print("\nPrimeiro número:", num1)
print("Segundo número:", num2)
print("Operador escolhido:", operador)
print("Resultado:", resultado)










