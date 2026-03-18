from database.connect import ConnectDatabase


class SQLUpdate:
    def __init__(self):
        self.conn = ConnectDatabase()
        self.conn.conectar()

    def update_complaint_on_audience(self, complaint_id, audience_id):
        sql = """UPDATE denuncia 
                 SET audiencia_id = %s 
                 WHERE denuncia_id = %s"""
        dados = (audience_id, complaint_id)
        self.conn.execute_query(sql, dados)

    def update_person(self, name, phone, pessoa_id):
        sql = """UPDATE PESSOA 
                 SET nome = %s, telefone = %s 
                 WHERE pessoa_id = %s"""
        dados = (name, phone, pessoa_id)
        self.conn.execute_query(sql, dados)

    def update_address(self, rua, bairro, cidade, numero, endereco_id):
        sql = """UPDATE ENDERECO 
                 SET rua = %s, bairro = %s, cidade = %s, numero = %s 
                 WHERE endereco_id = %s"""
        dados = (rua, bairro, cidade, numero, endereco_id)
        self.conn.execute_query(sql, dados)

    def update_agreement(self, status_acordo, data_acordo, acordo_id):
        sql = """UPDATE ACORDO 
                 SET status_acordo = %s, data_acordo = %s 
                 WHERE acordo_id = %s"""
        dados = (status_acordo, data_acordo, acordo_id)
        self.conn.execute_query(sql, dados)

    def update_audience(self, status_audiencia, data_audiencia, audiencia_id):
        sql = """UPDATE AUDIENCIA 
                 SET status_audiencia = %s, data_audiencia = %s 
                 WHERE audiencia_id = %s"""
        dados = (status_audiencia, data_audiencia, audiencia_id)
        self.conn.execute_query(sql, dados)

    def update_mediator(self, status_mediador, mediador_id):
        sql = """UPDATE MEDIADOR 
                 SET status_mediador = %s 
                 WHERE mediador_id = %s"""
        dados = (status_mediador, mediador_id)
        self.conn.execute_query(sql, dados)

    def update_manager(self, status_gestor, gestor_id):
        sql = """UPDATE GESTOR 
                 SET status_gestor = %s 
                 WHERE gestor_id = %s"""
        dados = (status_gestor, gestor_id)
        self.conn.execute_query(sql, dados)
