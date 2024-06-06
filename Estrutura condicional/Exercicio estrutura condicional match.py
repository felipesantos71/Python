import os
import time

while True:
    numero = int(input("Digite um número de a 1 a 12: "))
    if numero < 1 or numero > 12:
        os.system("cls || clear")
        print("Digite um número válido!")
    match(numero):
        case 1:
            mes = "janeiro"
            break
        case 2:
            mes = "fevereiro"
            break
        case 3:
            mes = "março"
            break
        case 4:
            mes = "abril"
            break
        case 5:
            mes = "maio"
            break
        case 6:
            mes = "junho"
            break
        case 7:
            mes = "julho"
            break
        case 8:
            mes = "agosto"
            break
        case 9:
            mes = "setembro"
            break
        case 10:
            mes = "outubro"
            break
        case 11:
            mes = "novembro"
            break
        case 12:
            mes = "dezembro"
            break
        case _:
            time.sleep(1.2)
print(f"Mês: {mes}!")