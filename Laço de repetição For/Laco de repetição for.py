import os
os.system("cls || clear")

#Algoritmo: Números de 1 a 10.
for i in range(1,11):
    print(f"Número {i}")

#Algoritmo: Números de 10 a 1.
for i in range(10,0,-1):
    print(f"Número {i}")


#exemplo prático
("\n=== Solicitando dados do usuário ===")
numero = int(input("Digite um número: "))
for i in range(1,11):
    produto = i * numero
    print(f"Tabuada: {numero}x{i}: {produto}")