import os
from dataclasses import dataclass
os.system("cls || clear")
#constante
QUANTIDADE_ALUNOS = 2
#classe
@dataclass
class Aluno:
    nome:str
    idade:int
    altura:float
    peso:float

alunos = []

#solicitando dados do usuario
for i in range(QUANTIDADE_ALUNOS):
    nome_do_aluno = input("Digite seu nome:")
    idade_do_aluno = int(input("Digite sua idade: "))
    altura_do_aluno = float(input("Digite sua altura em metros: "))
    peso_do_aluno = float(input("Digite seu peso em KG: "))

    aluno = Aluno(nome = nome_do_aluno, idade = idade_do_aluno, 
    altura = altura_do_aluno, peso = peso_do_aluno) 
    alunos.append(aluno)

#exibindo dados para o usuário
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Altura: {i.altura}")
    print(f"Peso: {i.peso}")