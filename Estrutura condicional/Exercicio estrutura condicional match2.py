import os 
import time

while True:
    valor = float(input("Informe se deseja pagar a 1 - vista ou a 2 - prazo: "))
    if valor < 1 or valor > 2:
        os.system("cls || clear")
        print("Digite uma opção válida 1 ou 2.")
    match(valor):
        case 1:
            produto = 100.00
            formaPagamento = "À vista"
            desconto = 10
            total = 90.00
            break
        case 2:
            produto = 100.00
            formaPagamento = "À prazo"
            parcelas = 6
            valorParcela = 16.66
            total = 100.00
            break
        case _:
            time.sleep(1.2)
print(f"Valor do produto: R${produto}")
print(f"Forma de pagamento: {formaPagamento}")
if valor == 1:
    print(f"Desconto: R${desconto}")
else:
    print(f"Parcelas: {parcelas}")
    print(f"Valor das parcelas: R${valorParcela}")
print(f"Valor final do produto: R${total}")
