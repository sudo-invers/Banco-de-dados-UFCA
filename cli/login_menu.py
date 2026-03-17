import toml

from cli.menu import menuCLI
from database.connect import ConnectDatabase


class LoginMenu:
    """
    Menu para realizar o login do usuario no sistema
    """

    def menu(self):
        """
        Menu de login
        """
        while True:
            print("\n=== LOGIN ===")
            print("1 - Entrar")
            print("2 - Utilizar ultimo login")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))

            if opcao.is_integer() is False or opcao < 0 or opcao > 2:
                print(f"Opcão '{opcao}' invalida, tente novamente")

            elif opcao == 1:
                self.__login()
                menuCLI().menu_principal()
                break
            elif opcao == 2:
                menuCLI().menu_principal()
            elif opcao == 0:
                break

    def __login(self):
        """Faz o login, pedindo usuario e senha"""
        config = toml.load("database/config.toml")
        while True:
            nome = input("Nome do usuário (Padrão: postgres): ")
            if nome.strip() == "":
                print("Nome nao pode ser vazio")
                break
            senha = input("Senha: ")
            if senha.strip() == "":
                print("Senha nao pode ser vazia")
                break
            print("Fazendo login, aguarde...")
            config["database"]["user"] = nome
            config["database"]["password"] = senha

            with open("database/config.toml", "w") as f:
                toml.dump(config, f)

            print("Conectando ao banco de dados")
            return ConnectDatabase().conectar(nome, senha)
