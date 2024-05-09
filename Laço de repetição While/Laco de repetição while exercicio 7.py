import os
import time

somaPar = 0
somaGeral = 0
mediaPar = 0
mediaGeral = 0
impar = 0
par = 0
contador = 0

while True:
    numero = float(input("Digite um número positivo: "))
    if numero > 0 :
        somaGeral+=numero
        contador+=1
        if numero % 2 == 0:
            somaPar += numero
            par+=1
        else:
            impar+=1
    else:
        if contador == 0:
            print("Digite novamento um número positivo.")
            time.sleep(2)
        else:
            break

mediaGeral=somaGeral/contador

if somaPar!= 0:
    mediaPar=somaPar/par
else:
    mediaPar=0    


print(f"Números pares: {par}")
print(f"Números impares: {impar}")
print(f"Media dos números pares: {mediaPar}")
print(f"Média Geral: {mediaGeral}")

