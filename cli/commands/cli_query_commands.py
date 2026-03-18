import sys
from datetime import date, datetime

from cli.curr_user import user, set_user
from database.querys.sql_querys import SQLQuery


class CLIQueryCommand:
    '''A Classe mostra as informações que o usuário deve inserir para poder realizar consultas específicas no sistema.'''

    def __init__(self):
        self.repo = SQLQuery()

    # --- MÉTODOS AUXILIARES DE FORMATAÇÃO ---

    def _print_denuncia(self, linha: tuple):
        print("-" * 50)
        print(f"   Denúncia ID : {linha[0]}")
        print(f"   Audiência ID: {linha[1] if linha[1] else 'Não agendada'}")
        print(f"   Acusador ID : {linha[2]}")
        print(f"   Acusado ID  : {linha[3]}")
        print(f"   Causa       : {linha[4]}")
        print(f"   Detalhes    : {linha[5] if linha[5] else 'Nenhum'}")
        print(f"   Data        : {linha[6]}")

    def _print_audiencia(self, linha: tuple):
        print("-" * 50)
        print(f"   Audiência ID : {linha[0]}")
        print(f"   Mediador ID  : {linha[1]}")
        print(f"   Endereço ID  : {linha[2]}")
        print(f"   Status       : {linha[3]}")
        print(f"   Data         : {linha[4]}")

    def _print_prefeitura(self, linha: tuple):
        print("-" * 50)
        print(f"   Prefeitura ID: {linha[0]}")
        print(f"   Endereço ID  : {linha[1]}")
        print(f"   CNPJ         : {linha[2]}")

    # --- COMANDOS DA CLI ---

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

        print(f"\nLogin realizado com sucesso! Bem-vindo(a), {user['email']}")

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

            if not resultado:
                print("\nNenhuma audiência encontrada para esta data e local.")
                return

            print("\n=== Resultados da Busca por Audiências ===")
            for linha in resultado:
                self._print_audiencia(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_complaint_cause(self):
        causa_denuncia = input("Digite a causa da denúncia: ")
        try:
            resultado: list[tuple] = self.repo.get_complaint_cause(causa_denuncia)

            if not resultado:
                print("\nNenhuma denúncia encontrada com esta causa.")
                return

            print(f"\n=== Denúncias com causa: {causa_denuncia} ===")
            for linha in resultado:
                self._print_denuncia(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_complaint_date(self):
        data_input = input("Digite a data (AAAA-MM-DD) da Denúncia: ")
        data_denuncia: date = datetime.strptime(data_input, "%Y-%m-%d").date()

        try:
            resultado: list[tuple] = self.repo.get_complaint_of_date(data_denuncia)

            if not resultado:
                print("\nNenhuma denúncia encontrada para esta data.")
                return

            print(f"\n=== Denúncias cadastradas em {data_denuncia} ===")
            for linha in resultado:
                self._print_denuncia(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_complain_without_audience(self):
        try:
            resultado: list[tuple] = self.repo.get_complaint_without_audience()

            if not resultado:
                print("\nTodas as denúncias já possuem audiência agendada.")
                return

            print("\n=== Denúncias sem Audiência ===")
            for linha in resultado:
                self._print_denuncia(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_complaint_accused_name(self):
        nome: str = input("Digite o nome do acusado: ").strip()

        try:
            resultado: list[tuple] = self.repo.get_complaint_accused_name(nome)

            if not resultado:
                print(f"\nNenhuma denúncia encontrada para o acusado: {nome}.")
                return

            print(f"\n=== Denúncias contra: {nome} ===")
            for linha in resultado:
                self._print_denuncia(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_audience_for_accused(self):
        try:
            accused_id = int(input("Digite o ID do acusado: "))
            resultado: list[tuple] = self.repo.get_audience_for_accused(accused_id)

            if not resultado:
                print(f"\nNenhuma audiência encontrada para o acusado ID {accused_id}.")
                return

            print(f"\n=== Audiências do Acusado ID: {accused_id} ===")
            for linha in resultado:
                self._print_audiencia(linha)

        except ValueError:
            print("Erro: O ID deve ser um número inteiro.", file=sys.stderr)
        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_audience_for_accuser(self):
        try:
            accuser_id = int(input("Digite o ID do acusador: "))
            resultado: list[tuple] = self.repo.get_audience_for_accuser(accuser_id)

            if not resultado:
                print(f"\nNenhuma audiência encontrada para o acusador ID {accuser_id}.")
                return

            print(f"\n=== Audiências do Acusador ID: {accuser_id} ===")
            for linha in resultado:
                self._print_audiencia(linha)

        except ValueError:
            print("Erro: O ID deve ser um número inteiro.", file=sys.stderr)
        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_audience_without_agreement(self):
        try:
            resultado: list[tuple] = self.repo.get_audience_without_agreement()

            if not resultado:
                print("\nNenhuma audiência registrada como 'CONFLITO' (sem acordo).")
                return

            print("\n=== Audiências Sem Acordo (Conflito) ===")
            for linha in resultado:
                self._print_audiencia(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_query_mediator_city(self):
        city = input("Digite a cidade: ")
        try:
            resultado: list[tuple] = self.repo.get_mediator_by_city(city)

            if not resultado:
                print(f"\nNenhum mediador ativo encontrado na cidade de {city}.")
                return

            print(f"\n=== Mediadores Ativos em {city} ===")
            print("-" * 50)
            for linha in resultado:
                # Retorna apenas o nome do mediador
                print(f"Mediador: {linha[0]}")
            print("-" * 50)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)

    def cli_city_halls(self):
        try:
            resultado: list[tuple] = self.repo.get_city_halls()

            if not resultado:
                print("\nNenhuma prefeitura cadastrada.")
                return

            print("\n=== Prefeituras Cadastradas ===")
            for linha in resultado:
                self._print_prefeitura(linha)

        except Exception as e:
            print(f"Erro: {e}", file=sys.stderr)