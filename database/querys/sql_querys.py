from datetime import date
from database.connect import ConnectDatabase


class SQLQuery:
    """
    Classe responsável por consultas (SELECT) no banco de dados.

    Cada método retorna dados de acordo com critérios específicos.

    Retornos seguem o padrão:
        list[tuple] -> resultados da consulta
        None        -> em caso de erro
    """

    def __init__(self):
        """
        Inicializa a conexão com o banco de dados.
        """
        self.conn = ConnectDatabase()
        self.conn.conectar()

    def get_password_by_email(self, email: str) -> str | None:
        """
        Retorna a senha de um usuário pelo email.

        Args:
            email (str): Email do usuário.

        Returns:
            str: Senha do usuário.
            None: Se o usuário não existir ou houver erro.
        """
        sql_select: str = """
            SELECT senha
            FROM usuarios
            WHERE email = %s
        """
        dados: tuple = (email,)

        result = self.conn.get(sql_select, dados)

        if result and len(result) > 0:
            return result[0][0]

        return None

    def get_user_by_email(self, email: str) -> dict | None:
        """
        Busca um usuário pelo email, trazendo dados de:
            - usuarios
            - acusadores (se existir)
            - pessoas (dados pessoais)

        Args:
            email (str): Email do usuário

        Returns:
            dict: Dados do usuário com chaves:
                usuario_id, email, tipo_usuario,
                acusador_id, pessoa_id, nome, telefone, n_inscricao_tributaria, data_nascimento
            None: Se não encontrado ou erro
        """
        sql_select: str = """
            SELECT 
                u.usuario_id,
                u.email,
                u.tipo_usuario,
                a.acusador_id,
                p.pessoa_id,
                p.nome,
                p.telefone,
                p.n_inscricao_tributaria,
                p.data_nascimento
            FROM usuarios u
                LEFT JOIN acusadores a ON u.usuario_id = a.usuario_id
                LEFT JOIN pessoas p ON a.pessoa_id = p.pessoa_id
            WHERE u.email = %s
        """
        dados: tuple = (email,)

        result = self.conn.get(sql_select, dados)

        if result:
            # retorna como dicionário usando a primeira linha encontrada
            row = result[0]
            return {
                "usuario_id": row[0],
                "email": row[1],
                "tipo_usuario": row[2],
                "acusador_id": row[3],
                "pessoa_id": row[4],
                "nome": row[5],
                "telefone": row[6],
                "n_inscricao_tributaria": row[7],
                "data_nascimento": row[8],
            }

        return None

    def get_complaint_of_date(self, data_denuncia: date) -> list[tuple] | None:
        """
        Busca denúncias realizadas em uma data específica.

        Args:
            data_denuncia (date): Data da denúncia.

        Returns:
            list[tuple]: Lista de denúncias encontradas.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT *
            FROM denuncias
            WHERE data_denuncia = %s
        """
        dados: tuple = (data_denuncia,)
        return self.conn.get(sql_select, dados)

    def get_complaint_cause(self, causa_denuncia: str) -> list[tuple] | None:
        """
        Busca denúncias por causa/motivo.

        Args:
            causa_denuncia (str): Causa da denúncia.

        Returns:
            list[tuple]: Lista de denúncias encontradas.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT *
            FROM denuncias
            WHERE causa_denuncia = %s
        """
        dados: tuple = (causa_denuncia,)
        return self.conn.get(sql_select, dados)

    def get_complaint_cause_period(
        self, causa_denuncia: str, data_inicio: date, data_fim: date
    ) -> list[tuple] | None:
        """
        Busca denúncias por causa dentro de um período de datas.

        Args:
            causa_denuncia (str): Causa da denúncia.
            data_inicio (date): Data inicial do período.
            data_fim (date): Data final do período.

        Returns:
            list[tuple]: Lista de denúncias encontradas.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT *
            FROM denuncias
            WHERE causa_denuncia = %s
              AND (data_denuncia >= %s AND data_denuncia <= %s)
        """
        dados: tuple = (causa_denuncia, data_inicio, data_fim)
        return self.conn.get(sql_select, dados)

    def get_complaint_accused_name(self, name: str) -> list[tuple] | None:
        """
        Busca denúncias associadas a um acusado pelo nome.

        Args:
            name (str): Nome da pessoa acusada.

        Returns:
            list[tuple]: Lista de denúncias encontradas.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT d.*
            FROM denuncias d
                JOIN acusados a ON d.acusado_id = a.acusado_id
                JOIN pessoas p ON a.pessoa_id = p.pessoa_id
            WHERE p.nome = %s
        """
        dados: tuple = (name,)
        return self.conn.get(sql_select, dados)

    def get_mediator_by_city(self, city: str) -> list[tuple] | None:
        """
        Busca mediadores ativos em uma determinada cidade.

        Args:
            city (str): Nome da cidade.

        Returns:
            list[tuple]: Lista de nomes dos mediadores.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT pessoas.nome 
            FROM mediadores
                JOIN pessoas ON mediadores.pessoa_id = pessoas.pessoa_id
                JOIN prefeituras ON mediadores.prefeitura_id = prefeituras.prefeitura_id
                JOIN enderecos ON prefeituras.endereco_id = enderecos.endereco_id
            WHERE enderecos.cidade = %s
              AND mediadores.status_mediador = 'ATIVO'
        """
        dados: tuple = (city,)
        return self.conn.get(sql_select, dados)

    def get_audience_at_date_and_place(
        self, data_audiencia: date, rua: str, bairro: str, cidade: str
    ) -> list[tuple] | None:
        """
        Busca audiências em uma data e local específicos.

        Args:
            data_audiencia (date): Data da audiência.
            rua (str): Rua do endereço.
            bairro (str): Bairro do endereço.
            cidade (str): Cidade do endereço.

        Returns:
            list[tuple]: Lista de audiências encontradas.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT a.*
            FROM audiencias a
                JOIN enderecos e ON a.endereco_id = e.endereco_id
            WHERE a.data_audiencia = %s
              AND e.rua = %s
              AND e.bairro = %s
              AND e.cidade = %s
        """
        dados: tuple = (data_audiencia, rua, bairro, cidade)
        return self.conn.get(sql_select, dados)

    def get_audience_without_agreement(self) -> list[tuple] | None:
        """
        Busca audiências que possuem acordo com status de conflito.

        Returns:
            list[tuple]: Lista de audiências em conflito.
            None: Em caso de erro.
        """
        sql_select = """
            SELECT au.*
            FROM audiencias au
                JOIN acordos ac ON au.audiencia_id = ac.audiencia_id
            WHERE ac.status_acordo = 'CONFLITO'
        """
        return self.conn.get(sql_select, params=None)

    def get_complaint_without_audience(self) -> list[tuple] | None:
        """
        Busca denúncias que ainda não possuem audiência associada.

        Returns:
            list[tuple]: Lista de denúncias sem audiência.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT *
            FROM denuncias
            WHERE audiencia_id IS NULL
        """
        return self.conn.get(sql_select, None)

    def get_city_halls(self) -> list[tuple] | None:
        """
        Retorna todas as prefeituras cadastradas.

        Returns:
            list[tuple]: Lista de prefeituras.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT *
            FROM prefeituras
        """
        return self.conn.get(sql_select, params=None)

    def get_audience_for_accuser(self, accuser_id: int) -> list[tuple] | None:
        """
        Busca audiências associadas a um acusador.

        Args:
            accuser_id (int): ID do acusador.

        Returns:
            list[tuple]: Lista de audiências.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT a.*
            FROM audiencias a
                JOIN denuncias d ON a.audiencia_id = d.audiencia_id
            WHERE d.acusador_id = %s
        """
        dados: tuple = (accuser_id,)
        return self.conn.get(sql_select, dados)

    def get_audience_for_accused(self, accused_id: int) -> list[tuple] | None:
        """
        Busca audiências associadas a um acusado.

        Args:
            accused_id (int): ID do acusado.

        Returns:
            list[tuple]: Lista de audiências.
            None: Em caso de erro.
        """
        sql_select: str = """
            SELECT a.*
            FROM audiencias a
                JOIN denuncias d ON a.audiencia_id = d.audiencia_id
            WHERE d.acusado_id = %s
        """
        dados: tuple = (accused_id,)
        return self.conn.get(sql_select, dados)
