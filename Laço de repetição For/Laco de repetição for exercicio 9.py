import os
import sys

print("\n== Numeros inteiros Soma ==")

pares = 0
impares = 0
numero = []
numerosPares = []
numerosImpares = []

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
                numerosPares.append(numeroInteiro)
            else:
                impares+=1
                numerosImpares.append(numeroInteiro)
        break

for i, numeroInteiro in enumerate(numerosPares):
    print(f"{i+1}º número par: {numeroInteiro}")

for i, numeroInteiro in enumerate(numerosImpares):
    print(f"{i+1}º número impar: {numeroInteiro}")

soma = sum(numero)
print(f"Soma dos números inteiros: {soma}")
print(f"Quantidade pares: {pares}")
print(f"Quantidade impares: {impares}")