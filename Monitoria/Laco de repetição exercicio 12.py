import os

QUANTIDADE_NUMEROS = 4
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    while True:
        nota = int(input(f"Digite a {i+1}º nota: "))
        if nota < 0 or nota > 10:
            print("Digite um numero valido entre 0 e 10!")
        else:
            numeros.append(nota)
            break
quantidadeVetor = len(numeros)
somaVetor = sum(numeros)
mediaGeral = somaVetor/quantidadeVetor
print(f"Media geral: {mediaGeral}")
