from database.connect import ConnectDatabase


class insert:
    def __init__(self):
        self.conn = ConnectDatabase()
        self.conn.conectar()

    def insert_adress(self, rua: str, bairro: str, cidade: str, numero: str):
        sql_adress = """insert_ INTO endereco(rua, bairro, cidade, numero) VALUES (%s, %s, %s, %s);"""
        adress = (rua, bairro, cidade, numero)

        return self.conn.insert(sql_adress, adress)

    # inserção de pessoa
    def insert_people(self, id_endereco, nome, telefone, documento, nascimento):
        sql_insert = """INSERT INTO pessoa(id_endereco, nome, telefone, n_inscricao_tributaria, data_nascimento) VALUES
            (%s, %s, %s, %s, %s)"""
        people = (id_endereco, nome, telefone, documento, nascimento)

        return self.conn.insert(sql_insert, people)

    # cadastro de usuario
    def insert_user(self, id, email, senha, perfil):

        sql_insert = """INSERT INTO usuario(usuario_id, email, senha, tipo_usuario) values(%s, %s, %s, %s)"""
        user = (id, email, senha, perfil)

        return self.conn.insert(sql_insert, user)

    # Cadastrar acusador
    def insert_accuser(self, pessoa_id, usuario_id):

        sql_insert = """INSERT INTO acusador(pessoa_id, usuario_id) values(%s, %s)"""
        accuser = (pessoa_id, usuario_id)

        return self.conn.insert(sql_insert, accuser)

    # Cadastrar acusado
    def insert_accused(self, pessoa_id: int):
        sql_insert = """INSERT INTO acusado(pessoa_id) values(%s)"""
        accused = tuple([pessoa_id])
        return self.conn.insert(sql_insert, accused)

    # Cadastrar mediador
    def insert_mediator(self, pessoa_id, usuario_id, prefeitura_id, status):
        sql_insert = """INSERT INTO
            mediador(pessoa_id, usuario_id, prefeitura_id, status_mediador)
            values(%s, %s, %s, %s)"""
        mediator = (pessoa_id, usuario_id, prefeitura_id, status)

        return self.conn.insert(sql_insert, mediator)

    # Cadastrar gestor
    def insert_gestor(self, pessoa_id, usuario_id, prefeitura_id, status):
        sql_insert = """INSERT INTO
            gestor(prefeitura_id, usuario_id, pessoa_id, status_gestor)
            values(%s, %s, %s, %s)"""
        gestor = (prefeitura_id, usuario_id, pessoa_id, status)

        return self.conn.insert(sql_insert, gestor)

    # Cadastrar denúncia
    def insert_complaint(
        self, audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data
    ):
        sql_insert = """INSERT INTO
            denuncia(audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data_denuncia)
            values(%s, %s, %s, %s, %s, %s)"""
        complaint = (
            audiencia_id,
            acusador_id,
            acusado_id,
            causa_denuncia,
            detalhamento,
            data,
        )

        return self.conn.insert(sql_insert, complaint)

    # Cadastrar audiencia
    def insert_audience(self, id_mediador, id_endereco, status_audiencia, data):
        sql_insert = """INSERT INTO
            audiencia(mediador_id, endereco_id, status_audiencia, data_audiencia)
            values(%s, %s, %s, %s)"""
        audience = (id_mediador, id_endereco, status_audiencia, data)
        return self.conn.insert(sql_insert, audience)

    # Cadastrar acordo
    def insert_agreement(self, audiencia_id, status_acordo, data_acordo):
        sql_insert = """INSERT INTO
            acordo(audiencia_id, status_acordo, data_acordo)
            values(%s, %s, %s)"""
        agreement = (audiencia_id, status_acordo, data_acordo)
        return self.conn.insert(sql_insert, agreement)
