import os
os.system("cls || clear")

print("\n== While de Nota de 0 a 10 ==")

while True:
    nota = float(input(f"Digite uma nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida. A nota deve estar entre 0 a 10. Por favor, tente novamente.")
    else:
        print("Sua nota: ", nota)
        break
