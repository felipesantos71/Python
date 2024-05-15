import os
import time

print("\n== Qualificação de aposentadoria ==")

idadeMinima = 18

codigoEmpregado = input(str("Digite o seu código de funcionário: "))

while True:
    idade = int(input("Digite sua idade: "))
    if idade < 18 or idade > 100:
        print("Idade inválida digite novamente!")
    else:
        break

while True:
    tempoContribuicao = int(input("Digite seu tempo de serviço(anos): "))
    if tempoContribuicao < 0 or tempoContribuicao > 30:
        print("Digite um tempo de serviço entre 1 a 30")
        
    else:
        if idade-idadeMinima >= tempoContribuicao:
            print("Seu tempo de contribuição excede, devido a sua idade digite o tempo apropriado!")
            break


print(f"Código do funcionário: {codigoEmpregado}")
print(f"Idade do funcionário: {idade}")
print(f"Tempo de serviço do funcionário: {tempoContribuicao}")
if idade >= 65 or tempoContribuicao >= 30:
    print("Requerer aposentadoria!\n")
else:
    print("Não requerer aposentadoria!\n")
