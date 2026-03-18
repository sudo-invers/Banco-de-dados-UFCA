from datetime import date

from database.connect import ConnectDatabase


class SQLInsertion:
    def __init__(self):
        self.conn = ConnectDatabase()
        self.conn.conectar()

    def insert_address(self, rua: str, bairro: str, cidade: str, numero: str) -> int | bool:

        sql_insert: str = """
            INSERT INTO enderecos (rua, bairro, cidade, numero)
            VALUES (%s, %s, %s, %s)
            RETURNING endereco_id;
            """
        address: tuple = (rua, bairro, cidade, numero)

        return self.conn.insert(sql_insert, address)

    # inserção de pessoa
    def insert_people(
            self,
            endereco_id: int,
            nome: str,
            telefone: str,
            n_inscricao_tributaria: str,
            data_nascimento: date
    ) -> bool:

        sql_insert: str = """
            INSERT INTO pessoas (endereco_id, nome, telefone, n_inscricao_tributaria, data_nascimento)
            VALUES (%s, %s, %s, %s, %s)
            """
        people: tuple = (endereco_id, nome, telefone, n_inscricao_tributaria, data_nascimento)

        return self.conn.insert(sql_insert, people)

    # cadastro de usuario
    def insert_user(self, email: str, senha: str, tipo_usuario: str) -> bool:

        sql_insert: str = """
            INSERT INTO usuarios (email, senha, tipo_usuario)
            VALUES (%s, %s, %s)
            """
        user: tuple = (email, senha, tipo_usuario)

        return self.conn.insert(sql_insert, user)

    # Cadastrar acusador
    def insert_accuser(self, pessoa_id: int, usuario_id: int) -> bool:

        sql_insert: str = """
            INSERT INTO acusadores (pessoa_id, usuario_id)
            VALUES (%s, %s)
            """
        accuser: tuple = (pessoa_id, usuario_id)

        return self.conn.insert(sql_insert, accuser)

    # Cadastrar acusado
    def insert_accused(self, pessoa_id: int) -> bool:
        sql_insert: str = """
            INSERT INTO acusados (pessoa_id)
            VALUES (%s)
            """
        accused: tuple = (pessoa_id,)
        return self.conn.insert(sql_insert, accused)

    # Cadastrar mediador
    def insert_mediator(self, pessoa_id: int, usuario_id: int, prefeitura_id: int, status_mediador: str) -> bool:
        sql_insert: str = """
            INSERT INTO mediadores (pessoa_id, usuario_id, prefeitura_id, status_mediador)
            VALUES (%s, %s, %s, %s)"""
        mediator: tuple = (pessoa_id, usuario_id, prefeitura_id, status_mediador)

        return self.conn.insert(sql_insert, mediator)

    # Cadastrar gestor
    def insert_gestor(self, pessoa_id: int, usuario_id: int, prefeitura_id: int, status_gestor: str) -> bool:
        sql_insert: str = """
            INSERT INTO gestores(prefeitura_id, usuario_id, pessoa_id, status_gestor)
            VALUES (%s, %s, %s, %s)
            """
        gestor: tuple = (prefeitura_id, usuario_id, pessoa_id, status_gestor)

        return self.conn.insert(sql_insert, gestor)

    # Cadastrar denúncia
    def insert_complaint(
        self, audiencia_id: int | None, acusador_id: int, acusado_id: int, causa_denuncia: str, detalhamento: str, data: date
    ) -> bool:
        sql_insert: str = """
            INSERT INTO denuncias (audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data_denuncia)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
        complaint: tuple = (
            audiencia_id,
            acusador_id,
            acusado_id,
            causa_denuncia,
            detalhamento,
            data,
        )

        return self.conn.insert(sql_insert, complaint)

    # Cadastrar audiencia
    def insert_audience(self, id_mediador: int, id_endereco: int, status_audiencia: str, data: date) -> bool:
        sql_insert: str = """
            INSERT INTO audiencias (mediador_id, endereco_id, status_audiencia, data_audiencia)
            VALUES (%s, %s, %s, %s)
            """

        audience: tuple = (
            id_mediador,
            id_endereco,
            status_audiencia,
            data
        )
        return self.conn.insert(sql_insert, audience)

    # Cadastrar acordo
    def insert_agreement(self, audiencia_id: int, status_acordo: str, data_acordo: date) -> bool:
        sql_insert: str = """
            INSERT INTO acordos (audiencia_id, status_acordo, data_acordo)
            VALUES (%s, %s, %s)
            """
        agreement: tuple = (audiencia_id, status_acordo, data_acordo)
        return self.conn.insert(sql_insert, agreement)
