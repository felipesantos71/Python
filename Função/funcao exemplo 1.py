import os
#Função sem retorno.
def cabecalho():
    os.system("cls || clear")
    print("=== SENAI ===")

cabecalho()
nome = str(input("Digite seu nome: "))
cabecalho()
idade = int(input("Digite sua idade: "))
cabecalho()
peso = float(input("Digite seu peso: "))