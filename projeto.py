class Usuario:
    def __init__(self, usuario, senha):
        self.username = usuario
        self.password = senha

class Funcionario(Usuario):
    def __init__(self, usuario, senha, nome):
        super().__init__(usuario, senha)
        self.nome = nome

    def __str__(self):
        return f"Nome: {self.nome}, usuario: {self.usuario}"

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao



    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}"

def adicionar_livro(livros):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")

    livro = Livro(titulo, autor, ano_publicacao,)
    livros.append(livro)
    print("Livro adicionado com sucesso!\n")

def visualizar_livros(livros):
    if livros:
        print("Lista de livros cadastrados:\n")
        for livro in livros:
            print(livro)
    else:
        print("Nenhum livro cadastrado.\n")

def adicionar_funcionario(funcionarios):
    login = input("Digite o login do funcionário: ")
    senha = input("Digite a senha do funcionário: ")
    nome = input("Digite o nome do funcionário: ")
    funcionario = Funcionario(login, senha, nome)
    funcionarios.append(funcionario)
    print("Funcionário adicionado com sucesso!\n")

def visualizar_funcionarios(funcionarios):
    if funcionarios:
        print("Lista de funcionários cadastrados:\n")
        for funcionario in funcionarios:
            print(funcionario)
    else:
        print("Nenhum funcionário cadastrado.\n")

def main():
    funcionarios = []
    livros = []

    while True:
        print("Menu Principal")
        print("1. Adicionar Livro")
        print("2. Visualizar Livros")
        print("3. Cadastrar Funcionário")
        print("4. Visualizar Funcionários")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_livro(livros)
        elif opcao == '2':
            visualizar_livros(livros)
        elif opcao == '3':
            adicionar_funcionario(funcionarios)
        elif opcao == '4':
            visualizar_funcionarios(funcionarios)
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
