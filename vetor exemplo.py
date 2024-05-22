import os
os.system("cls || clear")

notas = []

while True:
    nota = float(input(f"Digite uma nota ou se deseja encerrar digite (0):"))
    if nota < 0 or nota > 10:
        print("Digite uma nota válida!")
    elif nota == 0:
        break
    else:
        notas.append(nota)
        
somaNotas = sum(notas)
quantidadeNotas = len(notas)
media = somaNotas/quantidadeNotas

for i, nota in enumerate(notas):
    print(f"{i+1}ª nota: {nota}")

print(f"Média: {media}")