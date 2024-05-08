import os
os.system("cls || clear")

print("\n== Média de 4 notas ==")

media = 0
soma = 0

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma+=nota

media = soma/4
print(f"Sua média total é: {media}")