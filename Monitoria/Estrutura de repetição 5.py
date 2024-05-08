import os
os.system("\n== Cardápio ==")

dia = ""

operacao = int(input(f"Digite um número de 1 a 7 para saber o dia da semana :" ))

match operacao:
    case 1:
        dia = "Domingo"
    case 2:
        dia = "Segunda-Feira"
    case 3:
        dia = "Terça-Feira"
    case 4:
        dia = "Quarta-Feira"
    case 5:
        dia = "Quinta-Feira"
    case 6:
        dia = "Sexta-Feira"
    case 7:
        dia = "Sábado"
    case _:
        print(f"Seleção inválida!")

print(f"Prato escolhidos: {dia}")

if dia == "Domingo" or dia == "Sábado":
    print(f"Final de semana!")
else:
    print(f"Dia útil!")