import os
os.system("cls || clear")

primeiroNumero = int(input(f"Digite o primeiro número: "))
segundoNumero = int(input(f"Digite o segundo número: "))
terceiroNumero = int(input(f"Digite o terceiro número: "))

maiorNumero = max(primeiroNumero, segundoNumero, terceiroNumero)
menorNumero = min(primeiroNumero, segundoNumero, terceiroNumero)

print(f"Números escolhidos: {primeiroNumero},{segundoNumero},{terceiroNumero}")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")