import os
#declarando constante
QUANTIDADE_NUMEROS = 5
#declarando vetor
numeros = []
#declarando variavell
#laco for solicitar dados
for i in range(QUANTIDADE_NUMEROS):
    numeroInteiro = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numeroInteiro)
    somaInteiro = sum(numeros)
#apresentando dados
for i, numeroInteiro in enumerate(numeros):
    print(f"{i+1}º numero: {numeroInteiro}")
print(f"Soma dos numeros inteiros: {somaInteiro}")
