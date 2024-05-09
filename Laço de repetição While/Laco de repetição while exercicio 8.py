import os
import time
import sys

os.system("cls || clear")

maiorIdade = 0
menorIdade = sys.maxsize
mulheres5k = 0
somaSalarios = 0
quantidadeSalarios = 0
mediaSalarios = 0

while True:
    print("==Descrição de Seleções==\n")
    print("1 - Adicionar pessoa\n")
    print("2 - Exibir Resultados\n")
    opcao = int(input("Digite a opção desejada: "))

    match(opcao):
        case 1:
            print("== Solicitando Dados ==\n")
            while True:
                idade = int(input("Digite a idade: "))
                if idade < 0:
                    print("Número inválido digite novamente.")
                    time.sleep(0.02)
                    os.system("clear")
                else:
                    break
            while True:
                sexo = input("Digite o sexo (M ou F): ")
                sexo = sexo.upper()
                if sexo != 'F' and sexo != 'M':
                    print("Sexo inválido digite novamente.")
                    time.sleep(0.02)
                    os.system("clear")
                else:
                    break
            while True:
                salario = float(input("Digite o salário: "))
                if salario < 0:
                    print("Salário inválido digite novamente.")
                    time.sleep(0.02)
                    os.system("clear")
                else:
                    break
           
            somaSalarios += salario
            quantidadeSalarios += 1

            maiorIdade = max(idade, maiorIdade)
            menorIdade = min(idade, menorIdade)

            if sexo == "F" and salario >= 5000:
                mulheres5k += 1

            if quantidadeSalarios != 0:
                mediaSalarios = somaSalarios / quantidadeSalarios

                time.sleep(0.02)
                os.system("clear")
       
        case 2:
            print("=== Mostrando resultados ===")
            print(f"Média de salários do grupo: {mediaSalarios}")
            print(f"Maior idade do grupo: {maiorIdade}")
            print(f"Menor idade do grupo: {menorIdade}")
            print(f"Mulheres com salário a partir de 5 mil: {mulheres5k}")
            break
        case _:
            print("Opção inválida. \nTente novamente.")
            time.sleep(0.02)
            os.system("clear")