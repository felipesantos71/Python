import os
os.system

print("\n== Login e senha ==")

while True:
    nome = str(input(f"Digite seu login: "))
    senha = str(input(f"Digite sua senha de acesso: "))
    
    if nome == "marta" and senha == "f123":
        print(f"Bem vindo!")
        break
    else:
        print(f"Login e senha inválidos tente novamente!")
   