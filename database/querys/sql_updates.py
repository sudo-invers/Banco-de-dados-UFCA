from datetime import date
from database.connect import ConnectDatabase


class SQLUpdate:
    """
    Classe responsável por operações de UPDATE no banco de dados.

    Cada método atualiza registros em tabelas específicas.

    Retornos seguem o padrão:
        bool -> True se a operação foi bem-sucedida
        None -> Em caso de erro
    """

    def __init__(self):
        """
        Inicializa a conexão com o banco de dados.
        """
        self.conn = ConnectDatabase()
        self.conn.conectar()

    def update_complaint_on_audience(self, complaint_id: int, audience_id: int) -> bool | None:
        """
        Atualiza o vínculo de uma denúncia com uma audiência.

        Args:
            complaint_id (int): ID da denúncia.
            audience_id (int): ID da audiência a ser associada.

        Returns:
            bool: True se a atualização foi bem-sucedida.
            None: Em caso de erro.
        """
        sql_update: str = """
            UPDATE denuncias
            SET audiencia_id = %s 
            WHERE denuncia_id = %s
        """
        dados: tuple = (audience_id, complaint_id)
        return self.conn.update(sql_update, dados)

    def update_person(self, name: str, phone: str, pessoa_id: int) -> bool | None:
        """
        Atualiza os dados de uma pessoa.

        Args:
            name (str): Novo nome da pessoa.
            phone (str): Novo telefone.
            pessoa_id (int): ID da pessoa a ser atualizada.

        Returns:
            bool: True se a atualização foi bem-sucedida.
            None: Em caso de erro.
        """
        sql_update: str = """
            UPDATE pessoas
            SET nome = %s, telefone = %s 
            WHERE pessoa_id = %s
        """
        dados: tuple = (name, phone, pessoa_id)
        return self.conn.update(sql_update, dados)

    def update_address(self, rua: str, bairro: str, cidade: str, numero: str, endereco_id: int) -> bool | None:
        """
        Atualiza os dados de um endereço.

        Args:
            rua (str): Nome da rua.
            bairro (str): Bairro.
            cidade (str): Cidade.
            numero (str): Número do endereço.
            endereco_id (int): ID do endereço a ser atualizado.

        Returns:
            bool: True se a atualização foi bem-sucedida.
            None: Em caso de erro.
        """
        sql_update: str = """
            UPDATE enderecos
            SET rua = %s, bairro = %s, cidade = %s, numero = %s 
            WHERE endereco_id = %s
        """
        dados: tuple = (rua, bairro, cidade, numero, endereco_id)
        return self.conn.update(sql_update, dados)

    def update_agreement(self, status_acordo: str, data_acordo: date, acordo_id: int) -> bool | None:
        """
        Atualiza os dados de um acordo.

        Args:
            status_acordo (str): Novo status do acordo.
            data_acordo (date): Nova data do acordo.
            acordo_id (int): ID do acordo a ser atualizado.

        Returns:
            bool: True se a atualização foi bem-sucedida.
            None: Em caso de erro.
        """
        sql_update: str = """
            UPDATE acordos
            SET status_acordo = %s, data_acordo = %s 
            WHERE acordo_id = %s
        """
        dados: tuple = (status_acordo, data_acordo, acordo_id)
        return self.conn.update(sql_update, dados)

    def update_audience(self, status_audiencia: str, data_audiencia: date, audiencia_id: int) -> bool | None:
        """
        Atualiza os dados de uma audiência.

        Args:
            status_audiencia (str): Novo status da audiência.
            data_audiencia (date): Nova data da audiência.
            audiencia_id (int): ID da audiência a ser atualizada.

        Returns:
            bool: True se a atualização foi bem-sucedida.
            None: Em caso de erro.
        """
        sql_update: str = """
            UPDATE audiencias
            SET status_audiencia = %s, data_audiencia = %s 
            WHERE audiencia_id = %s
        """
        dados: tuple = (status_audiencia, data_audiencia, audiencia_id)
        return self.conn.update(sql_update, dados)

    def update_mediator(self, status_mediador: str, mediador_id: int) -> bool | None:
        """
        Atualiza o status de um mediador.

        Args:
            status_mediador (str): Novo status do mediador.
            mediador_id (int): ID do mediador a ser atualizado.

        Returns:
            bool: True se a atualização foi bem-sucedida.
            None: Em caso de erro.
        """
        sql_update: str = """
            UPDATE mediadores 
            SET status_mediador = %s 
            WHERE mediador_id = %s
        """
        dados: tuple = (status_mediador, mediador_id)
        return self.conn.update(sql_update, dados)

    def update_manager(self, status_gestor: str, gestor_id: int) -> bool | None:
        """
        Atualiza o status de um gestor.

        Args:
            status_gestor (str): Novo status do gestor.
            gestor_id (int): ID do gestor a ser atualizado.

        Returns:
            bool: True se a atualização foi bem-sucedida.
            None: Em caso de erro.
        """
        sql_update: str = """
            UPDATE gestores
            SET status_gestor = %s 
            WHERE gestor_id = %s
        """
        dados: tuple = (status_gestor, gestor_id)
        return self.conn.update(sql_update, dados)