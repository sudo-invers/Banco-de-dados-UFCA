from cli.commands.cli_insert_commands import InsertCommandCLI
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
                return "Opção Inválida!"


    def menu_denuncias(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar denúncia")
            print("2 - Consultar quantidade de denuncias por periodo")
            print("3 - Consultar denuncias com mesma causa")
            print("4 - Consultar denucias com mesma causa no mesmo periodo")
            print("5 - Consultar denuncias com o meu nome: acusado")
            print("6 - Consultar denuncias que não tiveram audiência")
            print("0 - Sair")
            opcao_denuncia = (input("Escolha uma opção: "))
            if opcao_denuncia == "1":
                return


            elif opcao_denuncia == "2":
                return            


            elif opcao_denuncia == "3":
                return
            elif opcao_denuncia == "4":
                return
            
            elif opcao_denuncia == "5":
                return
            elif opcao_denuncia == "6":
                return
            else:
                return "Opção Inválida!"




    def menu_audiencia(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar audiencia")
            print("2 - Consultar audiencias realizadas em determinado periodo e local")
            print("3 - Consultar audiencias que nao tiveram acordo")
            print("4 - Consultar audiencias que estão marcadas para acusador / acusado / mediador")
            print("5 - Consultar audiencias que estão marcadas para acusado")
            print("0 - Sair")
            opcao_audiencia = (input("Escolha uma opção: "))
            if opcao_audiencia == "1":
                insert = InsertCommandCLI()
                insert.insert_audience()
            elif opcao_audiencia == "2":
                return            
            elif opcao_audiencia == "3":
                return
            elif opcao_audiencia == "4":
                return
            elif opcao_audiencia == "5":
                return
            elif opcao_audiencia == "0":
                break
            else:
                print("Opção inválida")
                continue


    def menu_mediador(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar mediador")
            print("2- Consultar mediadores da minha cidade - sem exibir dados sensiveis")
            print("0 - Sair")
            opcao_mediador = (input("Escolha uma opção: "))
            if opcao_mediador == "1":
                return
            elif opcao_mediador == "2":
                return   
            elif opcao_mediador == "0":
                break  
            else:
                return "Opção Inválida!"                  


    def menu_pessoa(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar pessoa")
            print("0 - Sair")
            opcao_pessoa = (input("Escolha uma opção: ")).strip()
            if opcao_pessoa == "1":   
                return       
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
                return       
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
                return       
            elif opcao_endereco == "0":
                break
            else:
                return "Opção Inválida!"


    def menu_prefeitura(self):
        while True: 
            print("\n=== MENU ===")
            print("1 - Cadastrar prefeitura")
            print("1 - Consultar prefeituras disponíveis - que usam o sistema")
            print("0 - Sair")
            opcao_acusador = (input("Escolha uma opção: ")).strip()
            if opcao_acusador == "1":   
                return       
            elif opcao_acusador == "0":
                break
            else:
                return "Opção Inválida!"


    def menu_acordo(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar acordo")
            print("0 - Sair")
            opcao_acordo = (input("Escolha uma opção: "))
            if opcao_acordo == "1":
                return 
            
            elif opcao_acordo == "0":
                break


            else:
                return "Opção Inválida!"


    def menu_usuario(self):
        while True:
            print("\n=== MENU ===")
            print("1 - Cadastrar usuário")
            print("0 - Sair")
            opcao_usuario = (input("Escolha uma opção: "))
            if opcao_usuario == "1":   
                return       
            elif opcao_usuario == "0":
                break
            else:
                return "Opção Inválida!"