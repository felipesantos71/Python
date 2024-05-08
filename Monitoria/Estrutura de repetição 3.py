import os
os.system("\n== Operações com dois Números ==")
# 
primeiroNumero = int(input(f"Digite o primeiro número:"))
segundoNumero = int(input(f"Digite o segundo número:"))

operacao = str(input(f"Digite a operação desejada (+, -, *, /) :" ))

match operacao:
    case '+':
        resultado = primeiroNumero + segundoNumero
    case '-':
        resultado = primeiroNumero - segundoNumero
    case '*':
        resultado = primeiroNumero * segundoNumero
    case '/':
        resultado = primeiroNumero / segundoNumero
    case _:
        print(f"Operação inválida!")

print(f"Números escolhidos: {primeiroNumero},{segundoNumero}")
print(f"Resultado da operação escolhida: {resultado}")