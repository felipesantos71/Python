import os
os.system("cls || clear")

print("\n== Numero impares e pares==")

impares = 0
pares = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        pares+=1
    else:
        impares+=1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")