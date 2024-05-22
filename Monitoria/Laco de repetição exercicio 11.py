import os

QUANTIDADE_INTEIROS = 5
numeros = []
pares = 0
impares = 0
for i in range(QUANTIDADE_INTEIROS):
        numeroInteiro = int(input("Digite um numero: "))
        if numeroInteiro % 2 == 0:
            pares+=1
        else:
            impares+=1
        numeros.append(numeroInteiro)
print(f"Numeros pares: {pares}")
print(f"Numeros ìmpares: {impares}")