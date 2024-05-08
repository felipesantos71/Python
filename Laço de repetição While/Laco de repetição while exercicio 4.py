import os
os.system("\n== While Nota Aritmetica com contador ==")

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    validador = str(input("Deseja inserir mais uma nota (se não Digite N): "))
    validador=validador.lower()
    contador+=1
    soma+=nota

    if validador == 'n':
        break

media = soma / contador

print(f"Sua média aritimética é: {media}")