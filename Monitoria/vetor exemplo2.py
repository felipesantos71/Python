import os
import sys
os.system("cls || clear")

numeros = []
maiorNumero = 0
menorNumero = sys.maxsize

while True:
    numero = int(input(f"Digite um número: "))
    if numero < 0:
            print("Digite um número válido!")
    elif numero == 0:
        break
    else:
        numeros.append(numero)
        maiorNumero = max(maiorNumero,numero)
        menorNumero = min(menorNumero, numero)
        

for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")

print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
