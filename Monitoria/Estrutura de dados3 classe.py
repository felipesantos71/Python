import os
os.system("cls || clear")
#constante
QUANTIDADE_LIVROS = 2
#classe
class Livraria:
    def __init__(self, tipo_livro, tipo_editor, numero_paginas:int, preco_livro:float):
        self.livro = tipo_livro
        self.editor = tipo_editor
        self.paginas = numero_paginas
        self.preco = preco_livro
    
livros = []

#solicitando dados do usuario
for i in range(QUANTIDADE_LIVROS):
    tipo_livro = input("Digite nome do livro:")
    tipo_editor = input("Digite nome da editora: ")
    numero_paginas = int(input("Digite o numero de páginas: "))
    preco_livro = float(input("Digite o preço do livro: "))
    livros.append(Livraria(tipo_livro, tipo_editor, numero_paginas, preco_livro))

#exibindo dados para o usuário
for i in livros:
    print(f"Livro: {i.livro}")
    print(f"Editor: {i.editor}")
    print(f"Número de páginas: {i.paginas}")
    print(f"Preço do livro: R${i.preco}")