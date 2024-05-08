import os
os.system("cls || clear")

print("\n== Média de 3 notas e Aprovação ==")

QUANTIDADE_NOTAS = 3
media = 0
soma = 0

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma+=nota


media = soma/QUANTIDADE_NOTAS

if(media>=7):
    resultado = "Aprovado!"
elif(media>=5):
    resultado = "Recuperação!"
else:
    resultado = "Reprovado!"

print(f"Sua média: {media}")
print(f"Situação do aluno: {resultado}")