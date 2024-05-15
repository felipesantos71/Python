import os

print("\n== Media de 4 notas ==")

notas = []

QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    while True:
        notAluno = float(input(f"Digite {i+1}ª nota: "))
        if notAluno < 0 or notAluno > 10:
            print("Digite uma nota entre 0 e 10! ")
        else:
            notas.append(notAluno)
            break

for i, notAluno in enumerate(notas):
    print(f"{i+1}º nota: {notAluno}")

somaNotas = sum(notas)
numeroNotas = len(notas)
media = somaNotas/numeroNotas

print(f"Média aluno: {media}")