import os
import time
os.system("clear || cls")

print("\n== Média e números inteiros ==")

contador = 0
soma: float = 0
nota: float = 0

while True:
    nota = float(input("Digite um número: "))
    if nota > 0:
        contador+=1
        soma+=nota
        time.sleep(2)
    else:
        if contador==0:
            print("Digite novamente.")
            time.sleep(2)
            os.system("clear")
        else:
            break    

media = soma / contador
print(f"Média aritimética: {media}")