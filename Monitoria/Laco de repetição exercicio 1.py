import os
import time

print("\n== Número maior que 10 ==")

while True:
    numero = int(input("Digite um número: "))

    if numero > 10:
        print("É MAIOR QUE 10!")
        break
    elif numero == 10:
        print("É IGUAL A 10!")
    else:
        print("É MENOR QUE 10!")
