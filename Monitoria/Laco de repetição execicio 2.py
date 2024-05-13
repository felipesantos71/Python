import os
import time

print("\n==Média de aluno==")

media_Total = 0
NOTAS_ALUNO = 3
soma = 0

nome = str(input("Digite seu nome: "))
while True:  
    idade = int(input("Digite sua idade: "))
    if idade < 0 or idade > 100:
        print("Idade inválida digite novamento!")
    else:
        break

for i in range(NOTAS_ALUNO):
    while True:
        notas = float(input(f"Digite sua {i+1}ª nota: "))
        if notas < 0 or notas > 10:
            print("Digite sua nota novamente!")
        else:
            soma+=notas
            break


media_Total = soma / NOTAS_ALUNO
print(f"\nNome do aluno: {nome}")
print(f"\nIdade do aluno: {idade}")        
print(f"Média do aluno: {media_Total}")

if media_Total >= 7:
    print("Você foi aprovado!")
else:
    print("Você foi Reprovado!")
