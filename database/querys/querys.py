from database.connect import ConnectDatabase


class Querys:
    def __init__(self):
        self.conn = ConnectDatabase()
        self.conn.conectar()

    def query_complaint_of_date(self, data):
        sql = """SELECT * FROM denuncia WHERE data = %s"""
        dados = (data,)
        return self.conn.get(sql, dados)

    def query_complaint_cause(self, cause):
        sql = """SELECT * FROM denuncia WHERE causa = %s"""
        dados = (cause,)
        return self.conn.get(sql, dados)

    def query_complaint_cause_period(self, causa, data_ini, data_fim):
        sql = """SELECT * FROM DENUNCIA 
                 WHERE causa = %s AND (data_denuncia >= %s AND data_denuncia <= %s)"""
        dados = (causa, data_ini, data_fim)
        return self.conn.get(sql, dados)

    def query_complaint_accused_name(self, name):
        sql = """SELECT d.* FROM DENUNCIA d
                 JOIN ACUSADO a ON d.acusado_id = a.acusado_id
                 WHERE a.nome = %s"""
        dados = (name,)
        return self.conn.get(sql, dados)

    def query_mediator_city(self, city):
        sql = """SELECT PESSOA.nome 
                 FROM MEDIADOR 
                 JOIN PESSOA ON MEDIADOR.pessoa_id = PESSOA.pessoa_id
                 JOIN PREFEITURA ON MEDIADOR.prefeitura_id = PREFEITURA.prefeitura_id
                 JOIN ENDERECO ON PREFEITURA.endereco_id = ENDERECO.endereco_id
                 WHERE ENDERECO.cidade = %s AND MEDIADOR.status_mediador = 'ATIVO'"""
        dados = (city,)
        return self.conn.get(sql, dados)

    def query_audience_at_date_and_place(self, date, place):
        sql = """SELECT * FROM AUDIENCIA WHERE data = %s AND local = %s"""
        dados = (date, place)
        return self.conn.get(sql, dados)

    def query_audience_without_agreement(self):
        sql = """SELECT audiencia_id FROM ACORDO WHERE status_acordo = 'conflito'"""
        return self.conn.get(sql, None)

    def query_complaint_without_audience(self):
        sql = """SELECT denuncia_id FROM DENUNCIA WHERE audiencia_id IS NULL"""
        return self.conn.get(sql, None)

    def query_town_halls(self):
        sql = """SELECT * FROM PREFEITURA"""
        return self.conn.get(sql, None)

    def query_audience_for_accuser(self, accuser_id):
        sql = """SELECT * FROM AUDIENCIA WHERE acusador_id = %s"""
        dados = (accuser_id,)
        return self.conn.get(sql, dados)

    def query_audience_for_accused(self, accused_id):
        sql = """SELECT * FROM AUDIENCIA WHERE acusado_id = %s"""
        dados = (accused_id,)
        return self.conn.get(sql, dados)
