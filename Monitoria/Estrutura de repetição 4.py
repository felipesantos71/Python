import os
os.system("\n== Cardápio ==")

prato = ""
valor = 0

print(f"== MENU ==")
print(f"1-Picanha ")
print(f"2-Lasanha ")
print(f"3-Strogonoff ")
print(f"4-Bife Acebolado ")
print(f"5-Pão com ovo ")
operacao = int(input(f"Digite o número do prato desejada (1, 2, 3, 4, 5) :" ))

match operacao:
    case 1:
        prato = "Picanha"
        valor = 25.00
    case 2:
        prato = "Lasanha"
        valor = 20.00
    case 3:
        prato = "Strogonoff"
        valor = 18.00
    case 4:
        prato = "Bife Acebolado"
        valor = 15.00
    case 5:
        prato = "Pão com ovo"
        valor = 5.00
    case _:
        print(f"Operação inválida!")

print(f"Prato escolhidos: {prato}")
print(f"Valor do prato R$: {valor}")