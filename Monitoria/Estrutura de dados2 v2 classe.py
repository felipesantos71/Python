import os
os.system("cls || clear")
#constante
QUANTIDADE_ALUNOS = 2
#classe
class Aluno:
    def __init__(self, nome_aluno:str, idade_aluno:int, altura_aluno:float, peso_aluno:float):
        self.nome = nome_aluno
        self.idade = idade_aluno
        self.altura = altura_aluno
        self.peso = peso_aluno

alunos = []

#solicitando dados do usuario
for i in range(QUANTIDADE_ALUNOS):
    nome_aluno = input("Digite seu nome:")
    idade_aluno = int(input("Digite sua idade: "))
    altura_aluno = float(input("Digite sua altura em metros: "))
    peso_aluno = float(input("Digite seu peso em KG: "))
    alunos.append(Aluno(nome_aluno, idade_aluno, altura_aluno, peso_aluno))

#exibindo dados para o usuário
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Altura: {i.altura}")
    print(f"Peso: {i.peso}")