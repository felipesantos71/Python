import os
import math
#funcao menu 
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")
#funcao de calculo do imc
def calcular_imc(peso_paciente, altura_paciente):
    return peso_paciente / math.pow(altura_paciente, 2)
#funcao de resultado baseado no imc
def resultado_imc(imc_paciente):
    if imc_paciente < 18.5:
        resultados_imcs = "Muito magro"
    elif imc_paciente < 25:
        resultados_imcs = "Peso normal"
    elif imc_paciente < 30:
        resultados_imcs = "Sobrepeso"
    elif imc_paciente < 35:
        resultados_imcs = "Obesidade grau I"
    elif imc_paciente < 40:
        resultados_imcs = "Obesidade grau II"
    else:
        resultados_imcs = "Obesidade grau III (mórbida)"
    return resultados_imcs
    
#definindo classes
class Usuario:
    def __init__(self, nome_paciente, sobrenome_paciente, idade_paciente:int,
        altura_paciente:float, peso_paciente:float, imc_paciente:float,
        resultados_imcs, nome_completo):
        self.nome = nome_paciente
        self.sobrenome = sobrenome_paciente
        self.nomeCompleto = nome_completo
        self.idade = idade_paciente
        self.altura = altura_paciente
        self.peso = peso_paciente
        self.imcs = imc_paciente
        self.resultados = resultados_imcs
#vetor para armazenar a classe
informacoes = []
#solicitando informacoes e calculando dados
while True:
    logoSenai()
    nome_paciente = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    if nome_paciente.lower() == 'sair':
        break
    
    sobrenome_paciente = input("Digite o sobrenome do usuário: ")
    idade_paciente = int(input("Digite a idade do usuário: "))
    altura_paciente = float(input("Digite a altura do usuário (em metros): "))
    peso_paciente = float(input("Digite o peso do usuário (em quilogramas): "))
    
    nome_completo = (nome_paciente + " " + sobrenome_paciente)
    
    imc_paciente = calcular_imc(peso_paciente, altura_paciente)
    
    resultados_imcs = resultado_imc(imc_paciente)
    
    informacoes.append(Usuario(nome_paciente, sobrenome_paciente, idade_paciente,
    altura_paciente, peso_paciente, imc_paciente, resultados_imcs, nome_completo))

logoSenai()
print("\nDados dos usuários: \n")
for i in informacoes:
    print(f"\n====================")
    print("Nome:", i.nome)
    print(f"Sobrenome:", i.sobrenome)
    print(f"Nome completo:", i.nomeCompleto)
    print(f"Idade:", i.idade)
    print(f"Altura:", i.altura, "metros")
    print(f"Peso:", i.peso, "quilogramas")
    print(f"IMC:", round(i.imcs, 2))
    print(f"Resultado:", i.resultados)