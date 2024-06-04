class Usuario:
    def __init__(self, usuario, senha):
        self.username = usuario
        self.password = senha

class Funcionario(Usuario):
    def __init__(self, usuario, senha, nome, cargo):
        super().__init__(usuario, senha)
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"Nome: {self.nome}, Usuario: {self.username}, Cargo: {self.cargo}"

class Cliente(Usuario):
    def __init__(self, usuario, senha, nome, email):
        super().__init__(usuario, senha)
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}"

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}"

def importar_usuarios():
    usuarios = []
    try:
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[3] == "Admin":
                    usuario = Funcionario(dados[0], dados[1], dados[2], dados[3])
                else:
                    usuario = Cliente(dados[0], dados[1], dados[2], dados[3])
                usuarios.append(usuario)
        print("Usuários importados com sucesso!\n")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao importar usuários: {e}")
    return usuarios

def importar_livros():
    livros = []
    try:
        with open("livros.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(",")
                livro = Livro(dados[0], dados[1], dados[2])
                livros.append(livro)
        print("Livros importados com sucesso!\n")
    except FileNotFoundError:
        print("Arquivo de livros não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao importar livros: {e}")
    return livros

def cadastrar_usuario(usuarios):
    try:
        tipo_usuario = input("Digite o tipo de usuário (Cliente/Admin): ").lower()
        username = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        nome = input("Digite o nome do usuário: ")

        if tipo_usuario == "cliente":
            email = input("Digite o e-mail do cliente: ")
            usuario = Cliente(username, senha, nome, email)
            usuarios.append(usuario)
            print("Cliente cadastrado com sucesso!\n")
        elif tipo_usuario == "admin":
            senha_admin = input("Digite a senha de administrador: ")
            if senha_admin == "admin123":
                usuario = Funcionario(username, senha, nome, "Admin")
                usuarios.append(usuario)
                print("Usuário administrador cadastrado com sucesso!\n")
            else:
                print("Senha de administrador incorreta. Não é possível cadastrar um administrador.\n")
        else:
            print("Tipo de usuário inválido. Tente novamente.\n")
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar usuário: {e}")

def login(usuarios):
    MAX_ATTEMPTS = 3
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        try:
            username_or_email = input("Digite o nome de usuário ou e-mail: ")
            senha = input("Digite a senha: ")

            for usuario in usuarios:
                if ((usuario.username.lower() == username_or_email.lower() or 
                    (isinstance(usuario, Cliente) and usuario.email.lower() == username_or_email.lower())) and 
                    usuario.password == senha):
                    print("Login bem-sucedido!\n")
                    return usuario

            attempts += 1
            remaining_attempts = MAX_ATTEMPTS - attempts
            if remaining_attempts > 0:
                print(f"Nome de usuário, e-mail ou senha incorretos. Você tem mais {remaining_attempts} tentativa(s).\n")
            else:
                print("Número máximo de tentativas atingido. Tente novamente mais tarde.\n")
                return None
        except Exception as e:
            print(f"Ocorreu um erro durante o login: {e}")

    return None

def adicionar_livro(livros, usuario_logado):
    try:
        if isinstance(usuario_logado, Funcionario) and usuario_logado.cargo == "Admin":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = input("Digite o ano de publicação do livro: ")

            livro = Livro(titulo, autor, ano_publicacao)
            livros.append(livro)

            print("Livro adicionado com sucesso!\n")
        else:
            print("Acesso negado. Somente administradores podem adicionar livros.\n")
    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o livro: {e}")

def visualizar_livros(livros):
    try:
        if livros:
            print("Lista de livros cadastrados:\n")
            for livro in livros:
                print(livro)
        else:
            print("Nenhum livro cadastrado.\n")
    except Exception as e:
        print(f"Ocorreu um erro ao visualizar os livros: {e}")

def main():
    usuarios = importar_usuarios()
    clientes = []
    livros = importar_livros()
    usuario_logado = None

    while True:
        print("Menu Principal")
        print("1. Cadastrar Usuário")
        print("2. Login")
        print("3. Adicionar Livro")
        print("4. Visualizar Livros")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            usuario_logado = login(usuarios + clientes)
            if usuario_logado:
                print(f"Bem-vindo, {usuario_logado.nome}!\n")
        elif opcao == '3':
            if usuario_logado:
                adicionar_livro(livros, usuario_logado)
            else:
                print("Você precisa estar logado para adicionar um livro.\n")
        elif opcao == '4':
            visualizar_livros(livros)
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
