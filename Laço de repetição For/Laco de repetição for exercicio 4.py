import os
os.system("cls || clear")

soma = 0

print("\n== Soma de 5 numeros==")

for i in range(1,6):
    numero = int(input(f"Digite o {i}º número: "))
    soma += numero

print(f"Soma dos números escolhidos: {soma}")