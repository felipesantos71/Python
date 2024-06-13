import os
os.system("cls || clear")
#constante
QUANTIDADE_ALUNOS = 2
#vetor
nomes = []
idades = []
#solicitando dados do usuario
for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade: "))

    nomes.append(nome)
    idades.append(idade)
#exibindo dados para o usuário
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}")
    print(f"Idade: {idades[i]}")