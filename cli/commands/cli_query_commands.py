import sys
from datetime import date, datetime

from cli.curr_user import user, set_user
from database.querys.sql_querys import SQLQuery


class CLIQueryCommand:
    '''A Classe mostra as informações que o usuário deve inserir para poder realizar consultas específicas no sistema.'''
    def __init__(self):
        self.repo = SQLQuery()

    def cli_query_login(self):
        email: str = input("Digite seu Email: ")
        senha_input: str = input("Digite sua senha: ")

        senha = self.repo.get_password_by_email(email)

        if senha is None:
            print("Usuário não encontrado!", file=sys.stderr)
            return

        if senha_input != senha:
            print("Senha incorreta!")
            return

        usuario_data = self.repo.get_user_by_email(email)

        if not usuario_data:
            print("Erro ao buscar dados do usuário!", file=sys.stderr)
            return

        # Atualiza o user global
        set_user(
            {
                "usuario_id": usuario_data.get("usuario_id"),
                "email": usuario_data.get("email"),
                "pessoa_id": usuario_data.get("pessoa_id"),
                "tipo_usuario": usuario_data.get("tipo_usuario"),
                "acusador_id": usuario_data.get("acusador_id")
            }
        )

        print(f"Login realizado com sucesso! Bem-vindo(a), {user['email']}")


    def cli_query_audience_date_and_place(self):

        data_input = input("Digite a data (AAAA-MM-DD) da Audiência: ")
        data_audiencia: date = datetime.strptime(data_input, "%Y-%m-%d").date()

        cidade: str = input("Cidade: ")
        bairro: str = input("Bairro: ")
        rua: str = input("Rua: ")

        try:
            resultado: list[tuple] = self.repo.get_audience_at_date_and_place(
                data_audiencia=data_audiencia,
                cidade=cidade,
                bairro=bairro,
                rua=rua
            )

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)


    def cli_query_complaint_cause(self):
        causa_denuncia = input("Digite a causa da denúncia: ")
        try:
            resultado: list[tuple] = self.repo.get_complaint_cause(causa_denuncia)

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)


    def cli_query_complaint_date(self):

        data_input = input("Digite a data (AAAA-MM-DD) da Audiência: ")
        data_denuncia: date = datetime.strptime(data_input, "%Y-%m-%d").date()

        try:
            resultado: list[tuple] = self.repo.get_complaint_of_date(data_denuncia)

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)


    def cli_query_complain_without_audience(self):
        try:
            resultado: list[tuple] = self.repo.get_complaint_without_audience()

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_complaint_accused_name(self):
        nome: str = input("Digite o id do acusado: ").strip()

        try:
            resultado: list[tuple] = self.repo.get_complaint_accused_name(nome)

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)


    def cli_query_audience_for_accused(self):
        accused_id = int(input("Digite o ID do acusado: "))
        try:
            resultado: list[tuple] = self.repo.get_audience_for_accused(accused_id)

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_audience_for_accuser(self):
        accuser_id = int(input("Digite o id do acusador: "))
        try:
            resultado: list[tuple] = self.repo.get_audience_for_accuser(accuser_id)

            for linha in resultado:
                print(linha)
        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_audience_without_agreement(self):
        try:
            resultado: list[tuple] = self.repo.get_audience_without_agreement()

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_mediator_city(self):
        city = input("Digite a cidade: ")
        try:
            resultado: list[tuple] = self.repo.get_mediator_by_city(city)

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_city_halls(self):
        try:
            resultado: list[tuple] = self.repo.get_city_halls()

            for linha in resultado:
                print(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)
