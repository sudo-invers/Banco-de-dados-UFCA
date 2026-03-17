from database.connect import ConnectDatabase


class Inserts:
    def __init__(self):
        self.conn = ConnectDatabase()
        self.conn.conectar()

    # def insert_adress(self, rua: str, bairro: str, cidade: str, numero: str):
    #     sql_adress = """INSERT INTO ENDERECO(rua, bairro, cidade, numero) VALUES (%s, %s, %s, %s);"""
    #     adress = list(rua, bairro, cidade, numero)
    #
    #     dados = self.conn.insert_one(sql_adress, adress)
    #     return dados
    #
    #
    #
    # # inserção de pessoa
    def insert_people(self, id_endereco, nome, telefone, documento, nascimento):
        sql_insert = """INSERT INTO pessoa(id_endereco, nome, telefone, n_inscricao_tributaria, data_nascimento) VALUES
            (%s, %s, %s, %s, %s)"""
        people = (id_endereco, nome, telefone, documento, nascimento)

        return self.conn.execute_query(sql_insert, people)

    # cadastro de usuario
    def insert_user(self, id, email, senha, perfil):

        sql_insert = """INSERT INTO usuario(usuario_id, email, senha, tipo_usuario) VALUES(%s, %s, %s, %s)"""
        user = (id, email, senha, perfil)

        self.conn.execute_query(sql_insert, user)

    # # Cadastrar acusador
    # def InsertAccuser:
    #     def __init__(self, pessoa_id, usuario_id):
    #         self.sql_insert = (
    #             """INSERT INTO ACUSADOR(pessoa_id, usuario_id) VALUES(%s, %s)"""
    #         )
    #         self.accuser = (pessoa_id, usuario_id)
    #
    #     def insert(self):
    #         dados = self.conn(self.sql_insert, self.accuser)
    #         return dados.save()
    #
    #
    # # Cadastrar acusado
    # def InsertAccused:
    #     def __init__(self, pessoa_id: int):
    #         print("dados: agora vai")
    #         self.sql_insert = """INSERT INTO ACUSADO(pessoa_id) VALUES(%s)"""
    #         self.accused = tuple([pessoa_id])
    #
    #
    #     def insert(self):  # Em self.accused, deve enviar tupla.
    #         print(f"dados:{self.sql_insert}")
    #         print(self.accused)
    #         dados = self.conn(self.sql_insert, self.accused)
    #         print(dados, "A")
    #         return dados.save()
    #
    #
    # # Cadastrar mediador
    # def InsertMediator:
    #     def __init__(self, pessoa_id, usuario_id, prefeitura_id, status):
    #         self.sql_insert = """INSERT INTO
    #         MEDIADOR(pessoa_id, usuario_id, prefeitura_id, status_mediador)
    #         VALUES(%s, %s, %s, %s)"""
    #         self.mediator = (pessoa_id, usuario_id, prefeitura_id, status)
    #
    #     def insert(self):
    #         dados = self.conn(self.sql_insert, self.mediator)
    #         return dados.save()
    #
    #
    # # Cadastrar gestor
    # def InsertGestor:
    #     def __init__(self, pessoa_id, usuario_id, prefeitura_id, status):
    #         self.sql_insert = """INSERT INTO
    #         GESTOR( prefeitura_id, usuario_id, pessoa_id, status_gestor)
    #         VALUES(%s, %s, %s, %s)"""
    #         self.gestor = (prefeitura_id, usuario_id, pessoa_id, status)
    #
    #     def insert(self):
    #         dados = self.conn(self.sql_insert, self.gestor)
    #         return dados.save()
    #
    #
    # # Cadastrar denúncia
    # def InsertComplaint:
    #     def __init__(
    #         self, audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data
    #     ):
    #         self.sql_insert = """INSERT INTO
    #         DENUNCIA(audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data_denuncia)
    #         VALUES(%s, %s, %s, %s, %s, %s)"""
    #         self.complaint = (
    #             audiencia_id,
    #             acusador_id,
    #             acusado_id,
    #             causa_denuncia,
    #             detalhamento,
    #             data,
    #         )
    #
    #     def insert(self):
    #         dados = self.conn(self.sql_insert, self.complaint)
    #         return dados.save()
    #
    #
    # # Cadastrar audiencia
    # def InsertAudience:
    #     def __init__(self, id_mediador, id_endereco, status_audiencia, data):
    #         self.sql_insert = """INSERT INTO
    #         AUDIENCIA(mediador_id, endereco_id, status_audiencia, data_audiencia)
    #         VALUES(%s, %s, %s, %s)"""
    #         self.audience = (id_mediador, id_endereco, status_audiencia, data)
    #
    #     def insert(self):
    #         dados = self.conn(self.sql_insert, self.audience)
    #         return dados.save()
    #
    #
    # # Cadastrar acordo
    # def InsertAgreement:
    #     def __init__(self, audiencia_id, status_acordo, data_acordo):
    #         self.sql_insert = """INSERT INTO
    #         ACORDO(audiencia_id, status_acordo, data_acordo)
    #         VALUES(%s, %s, %s)"""
    #         self.agreement = (audiencia_id, status_acordo, data_acordo)
    #
    #     def insert(self):
    #         dados = self.conn(self.sql_insert, self.agreement)
    #         return dados.save()
