import os
import time
os.system("\n== Dia da semana ==")

dia = ""
tipoDia = ""

while True:
    operacao = int(input(f"Digite um número de 1 a 7 para saber o dia da semana :" ))
    if operacao < 1 or operacao > 7:
        print("Escreva um numero entre 1 e 7.")
        time.sleep(1.1)
    match operacao:
        case 1:
            dia = "Domingo"
            break
        case 2:
            dia = "Segunda-Feira"
            break
        case 3:
            dia = "Terça-Feira"
            break
        case 4:
            dia = "Quarta-Feira"
            break
        case 5:
            dia = "Quinta-Feira"
            break
        case 6:
            dia = "Sexta-Feira"
            break
        case 7:
            dia = "Sábado"
            break
        case _:
            print(f"Seleção inválida!")

if dia == "Domingo" or dia == "Sábado":
    tipoDia = "Final de Semana"
else:
    tipoDia = "Dia útil"

os.system("clear || cls")
print(f"Dia da semana: {dia}")
print(f"É um: {tipoDia}")