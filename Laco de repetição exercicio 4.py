import os
import time
import sys

print("\n== 3 números ==")

numeroMaior = 0
numeroMenor = sys.maxsize
numeros = []

QUANTIDADE_NUMEROS = 3

for i in range(QUANTIDADE_NUMEROS):
    while True:
        numeroInteiro = int(input(f"Digite o {i+1} número: "))
        if numeroInteiro <0:
            print("Digite um número positivo!")
        else:
            numeros.append(numeroInteiro)
            numeroMaior = max(numeroInteiro, numeroMaior)
            numeroMenor = min(numeroInteiro, numeroMenor)
            break

for i, numeroInteiro in enumerate(numeros):
    print(f"{i+1}ª número: {numeroInteiro}")

if numeroMaior == numeroMenor:
    print("Números são iguais!")
else:
    print(f"Número maior: {numeroMaior}")
    print(f"Número menor: {numeroMenor}\n")


#comando somar vetor = sum(numeros)
#comando tamanho dos numeros do vetor = len(numeros)
#Definindo variavel soma para somar os numeros do vetor / soma = sum(numeros)
#Definindo quantidade de numeros usados no vetor para utilizar em uma variavel / tamanhoVetor = len(numeros)
#media de vetor = soma / tamanhoVetor