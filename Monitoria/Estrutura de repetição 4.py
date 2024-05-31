import os
import time
os.system("\n== Cardápio ==")

prato = ""
valor = 0
while True:
    print(f"== MENU ==")
    print(f"1-Picanha ")
    print(f"2-Lasanha ")
    print(f"3-Strogonoff ")
    print(f"4-Bife Acebolado ")
    print(f"5-Pão com ovo ")
    operacao = int(input(f"Digite o número do prato desejada (1, 2, 3, 4, 5) :" ))
    if operacao < 1 or operacao > 5:
        print("Digite uma opção válida entre 1 e 7! ")
        time.sleep(1.2)
        os.system("clear || cls")

    match operacao:
        case 1:
            prato = "Picanha"
            valor = 25.00
            break
        case 2:
            prato = "Lasanha"
            valor = 20.00
            break
        case 3:
            prato = "Strogonoff"
            valor = 18.00
            break
        case 4:
            prato = "Bife Acebolado"
            valor = 15.00
            break
        case 5:
            prato = "Pão com ovo"
            valor = 5.00
            break
        case _:
            print("")
            
os.system("clear || cls")
print(f"Prato escolhidos: {prato}")
print(f"Valor do prato R$: {valor}")