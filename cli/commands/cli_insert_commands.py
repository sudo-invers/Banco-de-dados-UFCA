from database.querys.inserts import InsertAccused, InsertAdress, InsertAudience, InsertAccuser, InsertAgreement, InsertComplaint, InsertGestor, InsertMediator, InsertPeople, InsertUser


class InsertCommandCLI:
    '''Classe 'CommandInserCLI' mostra os atributos que o usuário deve digitar na CLI para cadastrar os dados desejados, por meio 
    de chamadas às funções de database.'''


    def __init__(self):
        pass


    def insert_accused(self):
        pessoa_id = int(input("Digite o ID da pessoa: "))
        try:
            insercao = InsertAccused(pessoa_id)
            insercao.insert()
        except Exception as e:
            print("Erro ao cadastrar acusado:", e)


    def insert_adress(self):
        rua = (input("Rua: ")).strip()
        bairro = (input("Bairro: ")).strip
        cidade = (input("Cidade: ")).strip()
        numero = int(input("Numero: "))
        try:
            insersao = InsertAdress(rua, bairro, cidade, numero)
            insersao.insert()
        except Exception as e:
            print("Erro ao cadastrar endereco:", e)


    def insert_accuser(self):
        print("\n=== Cadastro de Acusador ===")
        pessoa_id = int(input("pessoa_id: "))
        usuario_id = int(input("usuario_id: "))
        try:
            inserscao = InsertAccuser(pessoa_id, usuario_id)
            inserscao.insert()
        except Exception as e:
            print("Erro ao cadastrar acusador:", e)


    def insert_audience(self):
        print("\n=== Cadastro de Audiência ===")
        id_mediador = int(input("Id do mediador: "))
        id_endereco = int(input("Id do endereco: "))
        status_audiencia = input("status da audiencia: ")
        data = input("data da audiencia (AAAA-MM-DD): ")
        try:
            inserscao = InsertAudience(id_mediador, id_endereco, status_audiencia, data)
            inserscao.insert()
        except Exception as e:
            print("Erro ao cadastrar audiencia:", e)


    def insert_agreement(self):
        print("\n=== Cadastro de Acusador ===")
        audiencia_id = int(input("id da audiencia: "))
        status_acordo = input("status do acordo: ")
        data_acordo = input("data do acordo (AAAA-MM-DD): ")
        try:
            inserscao = InsertAgreement(audiencia_id, status_acordo, data_acordo)
            inserscao.insert()
        except Exception as e:
            print("Erro ao cadastrar acordo:", e)


    def insert_complaint(self):
        print("\n=== Cadastro de Denúncia ===")
        audiencia_id = int(input("id da audiencia: "))
        acusador_id = int(input("Id do endereco: "))
        acusado_id = int(input("Id do endereco: "))
        causa_denuncia = input("status da audiencia: ")
        detalhamento = input("status da audiencia: ")
        data = input("data: ")
        try:
            inserscao = InsertComplaint(audiencia_id, acusador_id, acusado_id,causa_denuncia, detalhamento, data)
            inserscao.insert()
        except Exception as e:
            print("Erro ao cadastrar denúncia:", e)


    def insert_gestor(self):
        print("\n=== Cadastro de Gestor ===")
        pessoa_id = int(input("Id da pessoa: "))
        usuario_id = int(input("Id do usuario: "))
        prefeitura_id = int(input("Id da prfeitura: "))
        status = input("status do gestor: ")


        try:
            insercao = InsertGestor(pessoa_id, usuario_id, prefeitura_id,status)
            insercao.insert()


        except Exception as e:
            print(print("Erro ao cadastrar gestor:", e))


    def insert_medidador(self):
        print("\n=== Cadastro de Audiência ===")
        pessoa_id = int(input("Id da pessoa: "))
        usuario_id = int(input("Id do usuario: "))
        prefeitura_id = int(input("Id da prfeitura: "))
        status = input("status do mediador: ")
        try:
            insercao = InsertMediator(pessoa_id, usuario_id, prefeitura_id, status)
            insercao.insert()
        except Exception as e:
            return "Erro ao cadastrar mediador:", e


    def insert_pessoa(self):
        print("\n=== Cadastro de Pessoa ===")
        nome = int(input("Nome: "))
        telefone = int(input("Telefone: "))
        documento = input("Documento da pessoa: ")
        nascimento = input("Data de nascimento (AAAA-MM-DD): ")
        try:
            insercao = InsertPeople(nome, telefone, documento, nascimento)
            insercao.insert()
        except Exception as e:
            return "Erro ao cadastrar pessoa:", e


    def insert_usuario(self):
        print("\n=== Cadastro de Usuário ===")
        email = input("Email: ")
        senha = input("Senha: ")
        perfil = input("Perfil: ")
        try:
            insercao = InsertUser(email, senha, perfil)
            insercao.insert()
        except Exception as e:
            return "Erro ao cadastrar usuário:", e