import os
os.system("cls || clear")

print("\n== While de Nota de 0 a 10 ==")

nota: float = -1

while nota >= 10 or nota <= 0:
    nota = float(input(f"Digite uma nota: "))

print(f"Sua nota: {nota}") 