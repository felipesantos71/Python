import os
os.system("cls || clear")

print("\n=== Solicitando dados ===")
pesoMorangos = float(input("Digite o peso dos morangos (em Kg): "))
pesoMacas = float(input("Digite o peso de maçãs (em Kg): "))

if pesoMorangos > 5:
    precoMorango = 2.50
else :
    precoMorango = 2.20

if pesoMacas < 5:
    preMacas = 1.80
else:
    precoMacas = 1.50

pesoTotal = pesoMorangos + pesoMacas
subTotal = (precoMorango * pesoMorangos) + (precoMacas * pesoMacas)

if pesoTotal > 8 or subTotal > 25:
    desconto = (subTotal * 0.10)

totalPagar = subTotal - desconto

print(f"\n=== Exibindo Resultados ===")
print(f"Peso em morangos (em Kg): {pesoMorangos}")
print(f"Peso em maçãs (em Kg): {pesoMacas}")
print(f"Soma dos pesos (em Kg): {pesoTotal}")
print(f"Subtotal: R$ {subTotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {totalPagar:.2f}")