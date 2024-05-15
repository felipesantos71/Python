import os 
import time

print("\n== Peso ideal ==")

while True:
    sexo = str(input("Digite seu sexo: "))
    if sexo == 'F' or sexo == 'M':
        sexo = sexo.upper()
        break
    else:
        print("Sexo inválido, use somente os caracteres 'F' ou 'M'! ")

while True:
    altura = float(input("Digite sua altura (em cm): "))
    if altura < 0 or altura > 220:
        print("Idade incorreta digite um valor em 1cm e 219cm! ")
    else:
        break

pesoIdealHomen = (72.7*altura)-58
pesoIdealMulher = (62.1*altura)-44.7

if sexo == 'F':
    print(f"Seu peso ideal é: {pesoIdealMulher}")
else:
    print(f"Seu peso ideal é: {pesoIdealHomen}") 
