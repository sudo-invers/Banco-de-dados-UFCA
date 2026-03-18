from cli.commands.cli_insert_commands import InsertCommandCLI
from cli.commands.cli_query_command import QueryCommand


class menuCLI:
    def __init__(self):
        pass

    def menu_principal(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Acusado")
            print("2 - Acusador")
            print("3 - Acordo")
            print("4 - Audiência")
            print("5 - Denuncia")
            print("6 - Endereço")
            print("7 - Mediador")
            print("8 - Prefeitura")
            print("9 - Pessoa")
            print("10 - Usuário")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.menu_acusado()

            elif opcao == "2":
                self.menu_acusador()

            elif opcao == "3":
                self.menu_acordo()

            elif opcao == "4":
                self.menu_audiencia()

            elif opcao == "5":
                self.menu_denuncias()

            elif opcao == "6":
                self.menu_endereco()

            elif opcao == "7":
                self.menu_mediador()

            elif opcao == "8":
                self.menu_prefeitura()

            elif opcao == "9":
                self.menu_pessoa()

            elif opcao == "10":
                self.menu_usuario()

            elif opcao == "0":
                break

            else:
                print("Opção inválida!")
                continue

    def menu_acusado(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Inserir Acusado")
            print("0 - Sair")

            opcao_acusado = (input("Escolha uma opção: ")).strip()

            if opcao_acusado == "1":
                op = InsertCommandCLI()
                op.insert_accused()

            elif opcao_acusado == "0":
                break

            else:
                print("Opção inválida!")
                continue

    def menu_denuncias(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar denúncia")
            print("2 - Consultar quantidade de denuncias por periodo")
            print("3 - Consultar denuncias com mesma causa")
            print("4 - Consultar denucias com mesma causa no mesmo periodo")
            print("5 - Consultar denuncias com o meu nome: acusado")
            print("6 - Consultar denuncias que não tiveram audiência")
            print("7 - Atualizar id da audiencia")
            print("0 - Sair")
            opcao_denuncia = input("Escolha uma opção: ")
            if opcao_denuncia == "1":
                consulta = InsertCommandCLI()
                consulta.insert_complaint()

            elif opcao_denuncia == "2":
                consulta = QueryCommand()
                consulta.cli_query_complaint_date()

            elif opcao_denuncia == "3":
                consulta = QueryCommand()
                consulta.cli_query_complaint_cause()

            elif opcao_denuncia == "4":
                pass

            elif opcao_denuncia == "5":
                consulta = QueryCommand()
                consulta.cli_complaint_accused_name()

            elif opcao_denuncia == "6":
                consulta = QueryCommand()
                consulta.cli_query_complain_without_audience()
            else:
                print("Opção inválida!")
                continue

    def menu_audiencia(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar audiencia")
            print("2 - Consultar audiencias realizadas em determinado periodo e local")
            print("3 - Consultar audiencias que nao tiveram acordo")
            print(
                "4 - Consultar audiencias que estão marcadas para acusador / acusado / mediador"
            )
            print("5 - Consultar audiencias que estão marcadas para acusado")
            print("0 - Sair")
            opcao_audiencia = input("Escolha uma opção: ")
            if opcao_audiencia == "1":
                insert = InsertCommandCLI()
                insert.insert_audience()

            elif opcao_audiencia == "2":
                consulta = QueryCommand()
                consulta.cli_query_audience_date_and_place()

            elif opcao_audiencia == "3":
                consulta = QueryCommand()
                consulta.cli_query_audience_without_agreement()

            elif opcao_audiencia == "4":
                pass

            elif opcao_audiencia == "5":
                pass

            elif opcao_audiencia == "0":
                break
            else:
                print("Opção inválida")
                continue

    def menu_mediador(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar mediador")
            print(
                "2- Consultar mediadores da minha cidade - sem exibir dados sensiveis"
            )
            print("0 - Sair")
            opcao_mediador = input("Escolha uma opção: ")

            if opcao_mediador == "1":
                consulta = InsertCommandCLI()
                consulta.insert_medidador()

            elif opcao_mediador == "2":
                consulta = QueryCommand()

                consulta.cli_query_mediator_city()
            elif opcao_mediador == "0":
                break

            else:
                print("Opção inválida!")
                continue

    def menu_pessoa(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar pessoa")
            print("0 - Sair")
            opcao_pessoa = (input("Escolha uma opção: ")).strip()

            if opcao_pessoa == "1":
                consulta = InsertCommandCLI()
                consulta.insert_pessoa()

            elif opcao_pessoa == "0":
                break

            else:
                return "Opção Inválida!"

    def menu_acusador(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar acusador")
            print("0 - Sair")
            opcao_acusador = (input("Escolha uma opção: ")).strip()

            if opcao_acusador == "1":
                consulta = InsertCommandCLI()
                consulta.insert_accuser()

            elif opcao_acusador == "0":
                break

            else:
                return "Opção Inválida!"

    def menu_endereco(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar endereco")
            print("0 - Sair")
            opcao_endereco = (input("Escolha uma opção: ")).strip()

            if opcao_endereco == "1":
                consulta = InsertCommandCLI()
                consulta.insert_adress()

            elif opcao_endereco == "0":
                break

            else:
                print("Opção inválida!")
                continue

    def menu_prefeitura(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar prefeitura")
            print("1 - Consultar prefeituras disponíveis - que usam o sistema")
            print("0 - Sair")
            opcao_prefeitura = (input("Escolha uma opção: ")).strip()

            if opcao_prefeitura == "1":
                pass

            elif opcao_prefeitura == "0":
                consulta = QueryCommand()
                consulta.cli_town_halls()

            elif opcao_prefeitura == "0":
                break

            else:
                print("Opção inválida!")
                continue

    def menu_acordo(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar acordo")
            print("0 - Sair")
            opcao_acordo = input("Escolha uma opção: ")

            if opcao_acordo == "1":
                consulta = InsertCommandCLI()
                consulta.insert_agreement()

            elif opcao_acordo == "0":
                break

            else:
                return "Opção Inválida!"

    def menu_usuario(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar usuário")
            print("0 - Sair")
            opcao_usuario = input("Escolha uma opção: ")

            if opcao_usuario == "1":
                consulta = InsertCommandCLI()
                consulta.insert_usuario()

            elif opcao_usuario == "0":
                break

            else:
                print("Opção inválida!")
                continue
