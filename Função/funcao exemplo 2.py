import os
os.system("cls || clear")

#Função com retorno
def somar(valor1, valor2):
    resultado = valor1 + valor2
    return resultado
def subtrair(valor1, valor2):
    resultado = valor1 - valor2
    return resultado
def multiplicar(valor1, valor2):
    return valor1 * valor2
def dividir(valor1, valor2):
    return valor1 / valor2

primeiroNumero = int(input("Digite seu primeiro numero: "))
segundoNumero = int(input("Digite seu segundo numero: "))

soma = somar(primeiroNumero, segundoNumero)
subtracao = subtrair(primeiroNumero, segundoNumero)
multiplicacao = multiplicar(primeiroNumero, segundoNumero)
divisao = dividir(primeiroNumero, segundoNumero)

print(f"")