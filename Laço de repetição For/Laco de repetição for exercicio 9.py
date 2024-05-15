import os
import sys

print("\n== Numeros inteiros Soma ==")

pares = 0
impares = 0
numero = []

NUMEROS_DIGITADOS = 5

for i in range(NUMEROS_DIGITADOS):
    while True:
        numeroInteiro = int(input(f"Digite o {i+1}º número: "))
        if numeroInteiro < 0:
            print("Digite um número válido!")
        else:
            numero.append(numeroInteiro)
            if numeroInteiro % 2 == 0:
                pares+=1
            else:
                impares+=1
        break

for i, numeroInteiro in enumerate(numero):
    print(f"{i+1} número: {numeroInteiro}")

soma = sum(numero)
print(f"Soma dos números inteiros: {soma}")
print(f"Números inteiros pares: {pares}")
print(f"Números inteiros impares: {impares}")