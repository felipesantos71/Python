import os
os.system("clear || cls")

print("\n== Média e números inteiros ==")

contador = 0
soma: float = 0

while True:
    numero = float(input(f"Digite um número: "))
    soma+=numero
    contador+=1
    
    if numero < 0:
        break

media = soma / contador

print(f"Média aritimética: {media}")