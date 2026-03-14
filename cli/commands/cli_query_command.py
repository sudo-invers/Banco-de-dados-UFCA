from database.querys.querys import QueryAudienceAtDateAndPlace, QueryAudienceForAccused, QueryAudienceForAccuser, QueryAudienceWithoutAgreement, QueryComplaintAccusedName, QueryComplaintCause, QueryComplaintOfDate, QueryComplaintWithoutAudience, QueryMediatorCity, QueryTownHalls


class QueryCommand:
    '''A Classe mostra as informações que o usuário deve inserir para poder realizar consultas específicas no sistema.'''
    def __init__(self):
        pass


    def cli_query_audience_date_and_place(self):
        date = input("Digite a data (AAAA-MM-DD) da Audiência: ")
        cause = input("Digite a causa da Audiência: ")
        try:
            consulta = QueryAudienceAtDateAndPlace(date, cause)
            resultado = consulta.con()


            for linha in resultado:
                print(linha)


        except Exception as e:
            print("Erro ao consultar audiências:", e)


    def cli_query_complaint_cause(self):
        cause = input("Digite a causa da denúncia: ")       
        try:
            consulta = QueryComplaintCause(cause)
            resultado = consulta.con()


            for linha in resultado:
                print(linha)


        except Exception as e:
            print("Erro ao consultar denúncias:", e)


    def cli_query_complaint_date(self):
        date = input("Digite a data (AAAA-MM-DD) da denúncia: ")      
        try:
            consulta = QueryComplaintOfDate(date)
            resultado = consulta.con()


            for linha in resultado:
                print(linha)


        except Exception as e:
            print("Erro ao consultar denúncias:", e)


    def cli_query_complain_without_audience(self):
        try:
            consulta = QueryComplaintWithoutAudience()
            resultado = consulta.con()
            for linha in resultado:
                print(linha)
        except Exception as e:
            print("Erro ao consultar denúncias:", e)