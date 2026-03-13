from connect import ConnectDatabase
from functools import wraps

connect = ConnectDatabase()

#consultas parametrizadas
#Consultar quantidade de denuncias por periodo

def decor(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # depois
        result = func(*args, **kwargs)
        # depois
        return result
    return wrapper

@decor
def func():
    return "oi"

class QueryComplaintOfDate:
    def __init__(self, data):
        self.sql_date_complaint = """SELECT * FROM DENUNCIA WHERE data = %s"""
        self.date_parameter = data


    def con(self) -> list[tuple]:
        connect.cur.execute(self.sql_date_complaint, (self.date_parameter,))
        self.query = connect.cur.fetchall()
        connect.close()
        return self.query

#Consultar denuncias com mesma causa 
class QueryComplaintCause:
    def __init__(self, cause):
        self.sql_cause_complaint = """SELECT * FROM DENUNCIA WHERE causa = %s"""
        self.cause_complaint = cause

    def con(self) -> list[tuple]:
        connect.cur.execute(self.sql_cause_complaint, (self.sql_cause_complaint,))
        self.query = connect.cur.fetchall()
        connect.close()
        return self.query
#Consultar denucias com mesma causa no mesmo periodo
#Consultar denuncias com o meu nome: acusado
class QueryComplaintAccusedName:
    def __init__(self, name):
        self.sql_accused_id_search = """SELECT acusado_id FROM ACUSADO WHERE nome = %s"""
        self.sql_accused_complaint = """SELECT * FROM DENUNCIA WHERE acusado_id = %s"""
        self.name_parameter = name
        
    def con(self):
        connect.cur.execute(self.sql_accused_id_search, (self.name_parameter,))
        self.id_accused = connect.cur.fetchone()
        connect.cur.execute(self.sql_accused_complaint, (self.id_accused[0],))
        self.query = connect.cur.fetchall()
        connect.close()
        return self.query

#Consultar mediadores da minha cidade - sem exibir dados sensiveis
class QueryMediatorCity():
    def __init__(self, city):
        self.sql_city_address_city_hall = """
                SELECT prefeitura_id
                FROM ENDERECO JOIN PREFEITURA
                    ON ENDERECO.endereco_id = PREFEITURA.endereco_id
                WHERE cidade = %s
                """
        self.sql_city_hall_mediator_user = """
                SELECT PESSOA.nome 
                FROM MEDIADOR JOIN PESSOA 
                    ON MEDIADOR.pessoa_id = PESSOA.pessoa_id
                WHERE status_mediador = 'ATIVO' AND prefeitura_id = %s"""
        self.city = city
        
    def con(self):
        connect.cur.execute(self.sql_city_address_city_hall, (self.city,))
        self.city_address = connect.cur.fetchone()
        if self.city_address:
            connect.cur.execute(self.sql_city_hall_mediator_user, (self.city_address[0],))
            self.query = connect.cur.fetchall()
            return self.query
        else:
            return []

#Consultar audiencias realizadas em determinado periodo e local
class QueryAudienceAtDateAndPlace():
    def __init__(self, date, place):
        self.sql_audience_date_place = """SELECT * FROM AUDIENCIA WHERE data = %s AND local = %s"""
        self.date_parameter = date
        self.place_parameter = place

    def con(self) -> list[tuple]:
        connect.cur.execute(self.sql_audience_date_place, (self.date_parameter, self.place_parameter),)
        self.query = connect.cur.fetchall()
        connect.close()
        return self.query
#Consultar audiencias que nao tiveram acordo
class QueryAudienceWithoutAgreement():
    def __init__(self):
        self.sql_audience_without_agreement ="""
            SELECT audiencia_id
            FROM ACORDO
            WHERE status_acordo = "conflito"
            """

    def con(self) -> list[tuple]:
        connect.cur.execute(self.sql_audience_without_agreement)
        self.query = connect.cur.fetchall()
        connect.close()
        return self.query
#Consultar denuncias que nao tiveram audiencia
class QueryComplaintWithoutAudience:
    def __init__(self):
        self.sql_complaint_without_audience = """
            SELECT audiencia_id
            FROM DENUNCIA
            WHERE audiencia_id = NULL
            """
        
    def con(self) -> list[tuple]:
        connect.cur.execute(self.sql_complaint_without_audience)
        self.query = connect.cur.fetchall()
        connect.close()
        return self.query
    
#Consultar locais com mais denuncias registradas

#Consultar prefeituras disponíveis - que usam o sistema
class QueryTownHalls:
    def __init__(self):
        self.sql_town_hall = """SELECT * FROM PREFEITURA"""

    def con(self) -> list[tuple]:
        connect.cur.execute(self.sql_town_hall)
        self.query = connect.cur.fetchall()
        connect.close()
        return self.query
#Consultar audiencias que estão marcadas para acusador / acusado / mediador
class QueryAudienceForAccuser():
    def __init__(self, accuser_id):
        pass
        
#Consultar audiencias que estão marcadas para acusado
class QueryAudienceForAccused():
    def __init__(self, accused_id):
        pass
