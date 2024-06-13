import os
os.system("cls || clear")
#classe
class Pets:
    def __init__(self, nome_pet, idade_pet:int, raca_pet, porte_pet, alimentacao_pet):
        self.nome = nome_pet
        self.idade = idade_pet
        self.raca = raca_pet
        self.porte = porte_pet
        self.alimentacao = alimentacao_pet
#vetor e constante
QUANTIDADE_PETS = 2
mascotes = []
#solicitando dados do usuario
for i in range(QUANTIDADE_PETS):
    nome_pet = input("Digite o nome do seu mascote: ")
    idade_pet = int(input("Digite a idade do mascote: "))
    raca_pet = input("Digite a raça de seu mascote:")
    porte_pet = input("Digite o porte do seu mascote: ")
    alimentacao_pet = input("Digite do que seu mascote se alimenta: ")
    mascotes.append(Pets(nome_pet, idade_pet, raca_pet, porte_pet, alimentacao_pet))
#apresentando dados ao usuario
os.system("cls || clear")
for i in mascotes:
    print(f"Nome do mascote: {i.nome}")
    print(f"Idade do mascote: {i.idade}")
    print(f"Raça do mascote: {i.raca}")
    print(f"Porte do mascote: {i.porte}")
    print(f"Alimentação do mascote: {i.alimentacao}")
