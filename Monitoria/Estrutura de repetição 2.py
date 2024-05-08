import os
os.system("cls || clear")

print(f"\n== Obrigatoriedade de voto ==")

idade = int(input(f"Digite sua idade: "))

if idade < 18 or idade >= 65:
    print(F"Você não é obrigado a votar!")
else:
    print(f"Você é obrigado a votar!")