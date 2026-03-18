import sys
from cli.commands.cli_insert_commands import CLIInsertCommand
from cli.commands.cli_query_commands import CLIQueryCommand

usuario: dict = {
    "usuario_id": None,
    "pessoa_id": None,
    "email": None,
    "senha": None,
    "tipo_usuario": None
}



class CLIMenu:
    """Menu interativo para navegação na CLI."""

    def __init__(self):
        # Instanciamos as classes apenas uma vez na inicialização
        self.insert_cmd = CLIInsertCommand()
        self.query_cmd = CLIQueryCommand()

    def menu_principal(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1 - Login")
            print("2 - Denúncias")
            print("3 - Audiências")
            print("4 - Prefeituras")
            print("5 - Acordos")
            print("6 - Mediadores")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.menu_login()
            elif opcao == "2":
                self.menu_denuncias()
            elif opcao == "3":
                self.menu_audiencia()
            elif opcao == "4":
                self.menu_prefeitura()
            elif opcao == "5":
                self.menu_acordo()
            elif opcao == "6":
                self.menu_mediador()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_login(self):
        pass

    def menu_denuncias(self):
        while True:
            print("\n=== MENU DENÚNCIAS ===")
            print("1 - Cadastrar denúncia")
            print("2 - Consultar denúncias por data")
            print("3 - Consultar denúncias por causa")
            print("4 - Consultar denúncias pelo ID do acusado")
            print("5 - Consultar denúncias que não tiveram audiência")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                try:
                    acusador_id = int(input("Digite o ID do Acusador para esta denúncia: "))
                    self.insert_cmd.insert_complaint(acusador_id)
                except ValueError:
                    print("Erro: O ID do acusador deve ser um número inteiro.", file=sys.stderr)
            elif opcao == "2":
                self.query_cmd.cli_query_complaint_date()
            elif opcao == "3":
                self.query_cmd.cli_query_complaint_cause()
            elif opcao == "4":
                self.query_cmd.cli_complaint_accused_name()
            elif opcao == "5":
                self.query_cmd.cli_query_complain_without_audience()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def menu_audiencia(self):
        while True:
            print("\n=== MENU AUDIÊNCIAS ===")
            print("1 - Cadastrar audiência")
            print("2 - Consultar audiências por data e local")
            print("3 - Consultar audiências que não tiveram acordo")
            print("4 - Consultar audiências do acusado")
            print("5 - Consultar audiências do acusador")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.insert_cmd.insert_audience()
            elif opcao == "2":
                self.query_cmd.cli_query_audience_date_and_place()
            elif opcao == "3":
                self.query_cmd.cli_query_audience_without_agreement()
            elif opcao == "4":
                self.query_cmd.cli_query_audience_for_accused()
            elif opcao == "5":
                self.query_cmd.cli_query_audience_for_accuser()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def menu_mediador(self):
        while True:
            print("\n=== MENU MEDIADORES ===")
            print("1 - Cadastrar mediador")
            print("2 - Consultar mediadores por cidade")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                try:
                    prefeitura_id = int(input("Digite o ID da Prefeitura vinculada: "))
                    usuario_id = int(input("Digite o ID do Usuário do mediador (ou 0 se não houver): "))
                    usuario_id = None if usuario_id == 0 else usuario_id

                    self.insert_cmd.insert_mediator(prefeitura_id, usuario_id)
                except ValueError:
                    print("Erro: IDs devem ser números inteiros.", file=sys.stderr)
            elif opcao == "2":
                self.query_cmd.cli_query_mediator_city()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def menu_prefeitura(self):
        while True:
            print("\n=== MENU PREFEITURAS ===")
            print("1 - Cadastrar prefeitura")
            print("2 - Consultar prefeituras cadastradas no sistema")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.insert_cmd.insert_cityhall()
            elif opcao == "2":
                self.query_cmd.cli_city_halls()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def menu_acordo(self):
        while True:
            print("\n=== MENU ACORDOS ===")
            print("1 - Cadastrar acordo")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.insert_cmd.insert_agreement()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")