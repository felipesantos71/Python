import os
import time
#definindo constante
QUANTIDADE_MEDIA = 3

#defindo vetor
notas = []

#definindo variaveis
quantidade_notas = 0
soma_nota = 0

#calculando média
def calcularMedia(notas):
    soma_nota = sum(notas)
    quantidade_notas = len(notas)
    media_total = soma_nota/quantidade_notas
    return media_total

#definindo situação de aprovação
def situacaoNota(media_aluno):
    if media_aluno >= 7:
        situacao = "Aprovado!"
    else:
        situacao = "Reprovado!"
    return situacao
    
#defindo funcao para apresentar dados ao usuario
def apresentar(situacao_aluno, media_aluno):
    print(f"Média: {round(media_aluno ,2)}")
    print(f"Situação: {situacao_aluno}")

#solicitando dados do usuario
for i in range(QUANTIDADE_MEDIA):
    while True:
        nota = float(input(f"Digite sua {i+1} nota: "))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            os.system("clear || cls")
            break
        else:
            print("Digite um valor acima entre 0 e 10.")
            time.sleep(0.5)
            os.system("clear || cls")

#apresentando dados ao usuario
for i, nota in enumerate(notas):
    print(f"{i+1}ª nota: {nota}")

media_aluno = calcularMedia(notas)
situacao_aluno = situacaoNota(media_aluno)
apresentar(situacao_aluno, media_aluno)