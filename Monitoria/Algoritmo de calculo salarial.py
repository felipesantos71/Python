import os
import time
import math

#funcao de cabecalho
def cabecalho():
    os.system("cls || clear")
    print("== SENAI ==")

login = "usuario123"
senha = "123456"

#solicitando senha de acesso
while True:
    loginAcesso = input("Digite seu login de acesso: ")
    senhaAcesso = input("Digite sua senha: ")
    if loginAcesso == login and senhaAcesso == senha:
        break
    else:
        print("Usuário ou senha inválidos tente novamente.")
        time.sleep(0.5)
        os.system("clear || cls")
    
#calculo de inss
def calculoInss(salario):
    if salario <= 1100:
        descontoInss = salario*0.075
    elif salario <= 2203.48:
        descontoInss = salario*0.09
    elif salario <= 3305.22:
        descontoInss = salario*0.12
    elif salario <= 6433.57:
        descontoInss = salario*0.14
    else:
        descontoInss = 854.36
    return descontoInss
    
#calculo irrf
def calculoIrrf(salario):
    if salario <= 2259.20:
        descontoIrrf = 0
        descontoirrfTotal = 0
    elif salario <= 2826.65:
        descontoIrrf = salario*0.075
        deducaoDependente = quantidadeDependentes*189.59
        descontoirrfTotal = descontoIrrf+deducaoDependente
    elif salario <= 3751.05:
        descontoIrrf = salario*0.15
        deducaoDependente = quantidadeDependentes*189.59
        descontoirrfTotal = descontoIrrf+deducaoDependente
    elif salario <= 4664.68:
        descontoIrrf = salario*0.225
        deducaoDependente = quantidadeDependentes*189.59
        descontoirrfTotal = descontoIrrf+deducaoDependente
    elif salario > 4664.68:
        descontoIrrf = salario*0.275
        deducaoDependente = quantidadeDependentes*189.59
        descontoirrfTotal = descontoIrrf+deducaoDependente
    return descontoirrfTotal
    
#calculo do vale transporte
def calculoTransporte(salario):
    if confirmarVale == 'S':
        descontoVale = salario*0.06
    return descontoVale
    
#calculo do vale refeição
def calculoRefeicao(salario):
    descontoRefeicao = valeRefeicao*0.2
    return descontoRefeicao
    
#calculo do plano de saude
def calculoSaude(salario):
    if dependentes == 'S':
        descontoplanoSaude = 150
        descontosaudeTotal = descontoplanoSaude*quantidadeDependentes
    else:
        descontosaudeTotal = 150
    return descontosaudeTotal
    
#solicitando dados o usuário
while True:
    salario = float(input("Digite seu salário: "))
    if salario < 1000:
        print("Digite um valor maior que R$ 1000.")
        time.sleep(0.5)
        os.system("clear || cls")
    else:
        break
while True:
    confirmarVale = input("Deseja ter vale tranporte Sim(S) ou Não(N): ").upper()
    if confirmarVale != 'S' and confirmarVale != 'N':
        print("Digite S ou N.")
        time.sleep(0.5)
        os.system("clear || cls")
    else:
        break
while True:
    valeRefeicao = float(input("Digite em R$ o vale refeição: "))
    if valeRefeicao < 0:
        print("Digite um valor maior que 0.")
        time.sleep(0.5)
        os.system("clear || cls")
    else:
        break
while True:
    dependentes = input("Você tem dependentes, SIM(S) ou NÃO(N): ").upper()
    if dependentes == 'S':
        quantidadeDependentes = int(input("Digite a quantidade de dependentes:"))
        break
    elif dependentes == 'N':
        quantidadeDependentes = 0
        break
    else:
        print("Digite S ou N.")
        time.sleep(0.5)
        os.system("clear || cls")
        
#calculo de descontos totais
if confirmarVale == 'S':
    descontoTotal = calculoInss(salario)+calculoIrrf(salario)+calculoTransporte(salario)+calculoRefeicao(salario)+calculoSaude(salario)
else:
    descontoTotal = calculoInss(salario)+calculoIrrf(salario)+calculoRefeicao(salario)+calculoSaude(salario)
salarioLiquido = salario - descontoTotal

#apresentando dados ao usuário
cabecalho()
print(f"Salário bruto: {salario}")
print(f"Desconto Inss: {round(calculoInss(salario), 2)}")
print(f"Desconto Irrf: {round(calculoIrrf(salario), 2)}")
if confirmarVale == 'S':
    print(f"Desconto transporte: {round(calculoTransporte(salario), 2)}")
print(f"Desconto vale refeição: {round(calculoRefeicao(salario), 2)}")
print(f"Desconto plano de saúde: {round(calculoSaude(salario), 2)}")
print(f"Sálario líquido: {round(salarioLiquido, 2)}")