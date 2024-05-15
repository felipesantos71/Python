import os
import time
import sys

print("\n==Números inteiros==")

QUANTIDADE_INTEIRO = 2
numeroMenor = sys.maxsize
numeroMaior = 0
produto = 0
media = 0
somaInteiro = 0

for i in range(QUANTIDADE_INTEIRO):
    while True:
        numeroInteiro = float(input(f"\nDigite o {i+1} número inteiro: "))
        if numeroInteiro <= 0:
            print("Digite um número maior que 0!")
        else:
            somaInteiro+=numeroInteiro
            numeroMaior = max(numeroInteiro, numeroMaior)
            numeroMenor = min(numeroInteiro, numeroMenor)
            break

produto = numeroMaior * numeroMenor
media = somaInteiro / QUANTIDADE_INTEIRO
print(f"\nMédia dos números: {media}")
print(f"Soma dos números: {somaInteiro}")
print(f"Produto dos números: {produto}")
if numeroMaior == numeroMenor:
    print(f"Os números são iguais. \n")
else:
    print(f"Menor número: {numeroMenor}")
    print(f"Maior número: {numeroMaior}\n")