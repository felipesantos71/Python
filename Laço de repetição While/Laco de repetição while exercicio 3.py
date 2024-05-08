import os
os.system("cls || clear")

print("\n== While nota com média e Aprovação ==")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida. A nota deve estar entre 0 a 10. Por favor, tente novamente.")
        else:
            soma+=nota
            break
        
media = soma / QUANTIDADE_NOTAS

if(media>=7):
    resultado = "Aprovado!"
elif(media>=5):
    resultado = "Recuperação!"
else:
    resultado = "Reprovado!"

print(f"Sua média: {media}")
print(f"Situação do aluno: {resultado}")