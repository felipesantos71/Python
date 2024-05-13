import os
import time

print("\n== Loja de maças ==")

precoMaca = 1.30
precoMacaAcima12 = 1

while True:
    compra = int(input("Digite o número de maças que deseja comprar:"))
    if compra < 0:
        print("Número de maças invalídas digite novamente!")
    else:
        break

if compra >= 12:
    total = compra*precoMacaAcima12
else:
    total = compra*precoMaca

print(f"Preço total das maças é: R$ {total}")