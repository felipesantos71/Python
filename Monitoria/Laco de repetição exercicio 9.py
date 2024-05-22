import os

QUANTIDADE_NOMES = 3
nomes = []

for i in range(QUANTIDADE_NOMES):
    nome = str(input("Digite um nome: "))
    nomes.append(nome)

for i, nome in enumerate(nomes):
    print(f"{i+1}º nome: {nome}")