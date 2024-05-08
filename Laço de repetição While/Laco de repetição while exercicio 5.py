import os
import time
os.system("cls || clear")

print("\n== Notas e medias com Menu de opções ==")

soma: float = 0
ContadorNotas = 0

while True:
    print(f"==  MENU ==")
    print(f"== S - Inserir mais uma nota; ==")
    print(f"== P - Ver quantas notas foram inseridas; ==")
    print(f"== N - Calcular a média aritimética das notas informadas. ==")
    validador = str(input("Digite uma das opçôes desejadas acima: "))
    validador = validador.lower()

    if validador == 's':
        nota = float(input(f"Digite uma nota: "))
        ContadorNotas+=1
        soma+=nota
        os.system("clear")
    elif validador == 'p':
        if ContadorNotas == 0:
            print(f"Não foram inseridas notas.")
            time.sleep(3)
            os.system("clear")
        else:
            print(f"Quantidade de notas inseridas: {ContadorNotas}")
            input(f"Pressione qualquer tecla para continuar...")
            os.system("clear")
    elif validador == 'n':
        if ContadorNotas == 0:
            print("Não foram inseridas notas. \n")
            time.sleep(3)
            os.system("clear")
        else:
            break
    else:
        print("Opção inválida... \n")
        time.sleep(3)
        os.system("clear")
             
media = soma / ContadorNotas
print(f"Média aritimética: {media}")
        

