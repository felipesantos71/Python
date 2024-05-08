import os
os.system("cls || clear")

print("\n== While nota com média e Aprovação ==")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite uma nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida. A nota deve estar entre 0 a 10. Por favor, tente novamente.")
        else:
            soma+=nota
            break
        
media = soma / QUANTIDADE_NOTAS
print(f"Sua média: {media}")

if(media>=7):
    print(f"Aprovado!")
elif(media>=4):
    print(f"Recuperação!")
else:
    print(f"Reprovado!")