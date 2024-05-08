import os
os.system("cls || clear")

print("\n== Média de 3 notas e Aprovação ==")

media = 0
soma = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma+=nota


media = soma/3
print(f"Sua média total é: {media}")

if(media>=7):
    print(f"Aprovado!")
elif(media>=4):
    print(f"Recuperação!")
else:
    print(f"Reprovado!")