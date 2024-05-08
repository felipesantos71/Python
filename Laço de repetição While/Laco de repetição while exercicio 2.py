import os
os.system("cls || clear")

print("\n== While nota com média ==")

soma = 0
contador = 0

while True:
    nota = float(input(f"Digite uma nota: "))
    soma+=nota
    contador+=1

    if contador > 1:
        break
        
media = soma / contador 
print(f"Sua média: {media}")

