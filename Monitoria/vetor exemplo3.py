import os

os.system("cls || clear")

QUANTIDADE_NUMEROS = 6

numeros = []
numerosPares = []
numerosImpares = []
pares = 0
impares = 0

for i in range(QUANTIDADE_NUMEROS):
    while True:
        numero = int(input(f"Digite o {i+1}º número: "))
        if numero % 2 == 0:
            pares+=1
            numerosPares.append(numero)
            break
        else:
            impares+=1
            numerosImpares.append(numero)
            break
os.system("cls || clear")
for i, numero in enumerate(numerosPares):
    print(f"{i+1}º numero par: {numero}")

for i, numero in enumerate(numerosImpares):
    print(f"{i+1}º numero impar: {numero}")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")