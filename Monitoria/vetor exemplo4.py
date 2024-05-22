import os
import sys

os.system("cls || clear")
#declaração de constante
QUANTIDADE_NUMEROS = 5
#declaração de vetores
numeros = []
somaPar = []
somaImpar = []
#declaração de variável
maiorNumero = 0
menorNumero = sys.maxsize
quantidadeImpar = 0
quantidadePar = 0
quantidaPositivo = 0
quantidaNegativo = 0
mediaGeral = 0
mediaPar = 0
mediaImpar = 0

#laço for para definir numeros inseridos pelo usuario
for i in range(QUANTIDADE_NUMEROS):
    numeroInteiro = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numeroInteiro)
    #definindo se numero é par
    if numeroInteiro % 2 == 0:
        quantidadePar+=1
        somaPar.append(numeroInteiro)
    #definindo se numero é impar
    else:
        quantidadeImpar+=1
        somaImpar.append(numeroInteiro)
    #definindo se numero é negativo
    if numeroInteiro < 0:
        quantidaNegativo+=1
    #definindo se numero é positivo
    else:
        quantidaPositivo+=1
    #definindo maior e menor numero
    maiorNumero = max(maiorNumero, numeroInteiro)
    menorNumero = min(menorNumero, numeroInteiro)
    quantidadeVetor = len(numeros)
    somaVetor = sum(numeros)

#definindo se calculo de par ou impar for igual a 0, ele dar média 0.
if quantidadePar == 0:
    mediaPar = 0
else:
    mediaPar = sum(somaPar)/quantidadePar

if quantidadeImpar == 0:
    mediaImpar = 0
else:
    mediaImpar = sum(somaImpar)/quantidadeImpar

mediaGeral = somaVetor/quantidadeVetor
#apresentando resultados
os.system("clear || cls")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
print(f"Quantidade de números ímpares: {quantidadeImpar}")
print(f"Quantidade de números pares: {quantidadePar}")
print(f"Quantidade de numeros negativos: {quantidaNegativo}")
print(f"Quantidade de numeros positivos: {quantidaPositivo}")
print(f"Quantidade total de números digitados: {quantidadeVetor}")
print(f"Media de numeros pares: {mediaPar}")
print(f"Media de numeros impares: {mediaImpar}")
print(f"Media geral dos numeros: {mediaGeral}")

#apresentando numeros em ordem inversa
for i, numeroInteiro in enumerate(reversed(numeros)):
        print(f"{quantidadeVetor-i}º numero em ordem inversa: {numeroInteiro}")

'''
#funcao para reverter e reaproveitar o codigo.
def inverterlista(lista):
    for i, numeroInteiro in enumerate(reversed(numeros)):
        print(f"{quantidadeVetor-i}º numero em ordem inversa: {numeroInteiro}")
#mostrando a funcao lista
inverterlista(numeros)
'''