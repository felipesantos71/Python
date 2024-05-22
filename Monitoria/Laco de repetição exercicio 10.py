import os
import time
#funcao sem retorno
def limpareTempo(limpar):
    os.system("clear || cls")
    print("Aguarde...")
    time.sleep(2)
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
limpareTempo(numeroInteiro)
for i, numeroInteiro in enumerate(numeros):
    print(f"{i+1}º numero: {numeroInteiro}")
print(f"Soma dos numeros inteiros: {somaInteiro}")
