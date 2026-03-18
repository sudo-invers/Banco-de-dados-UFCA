from database.querys.sql_querys import QueryAudienceAtDateAndPlace, QueryAudienceForAccused, QueryAudienceForAccuser, QueryAudienceWithoutAgreement, QueryComplaintAccusedName, QueryComplaintCause, QueryComplaintOfDate, QueryComplaintWithoutAudience, QueryMediatorCity, QueryTownHalls


class CLIQueryCommand:
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

    def cli_complaint_accused_name(self):
        name = input("Digite o id do acusado: ").strip()
        try:
            consulta = QueryComplaintAccusedName(name)
            resultado = consulta.con()

            for linha in resultado:
                print(linha)

        except Exception as e:
            print("Erro ao consultar denúncias:", e)


    def cli_query_audience_for_acused(self):
        accused_id = int(input("Digite o id do acusado: "))
        try:
            consulta = QueryAudienceForAccused(accused_id)
            resultado = consulta.con()
            for linha in resultado:
                print(linha)
        except Exception as e:
            print("Erro ao consultar audiencia:", e)

    def cli_query_audience_for_acused(self):
        accuser_id = int(input("Digite o id do acusador: "))
        try:
            consulta = QueryAudienceForAccuser(accuser_id)
            resultado = consulta.con()
            for linha in resultado:
                print(linha)
        except Exception as e:
            print("Erro ao consultar audiencia:", e)

    def cli_query_audience_without_agreement(self):
        try:
            consulta = QueryAudienceWithoutAgreement()
            resultado = consulta.con()
            for linha in resultado:
                print(linha)
        except Exception as e:
            print("Erro ao consultar audiencia:", e)

    def cli_query_mediator_city(self):
        city = int(input("Digite a cidade: "))
        try:
            consulta = QueryMediatorCity(city)
            resultado = consulta.con()

            for linha in resultado:
                print(linha)

        except Exception as e:
            print("Erro ao consultar mediadores:", e)

    def cli_town_halls(self):
        try:
            consulta = QueryTownHalls()
            resultado = consulta.con()

            for linha in resultado:
                print(linha)

        except Exception as e:
            print("Erro ao consultar prefeituras", e)
