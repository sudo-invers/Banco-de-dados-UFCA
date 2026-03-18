from datetime import date
from database.connect import ConnectDatabase


class SQLInsertion:
    """
    Classe responsável por centralizar operações de INSERT no banco de dados.

    Cada método executa uma inserção em uma tabela específica e retorna
    o ID gerado pelo banco (usando RETURNING).

    Retornos seguem o padrão:
        int  -> sucesso (ID gerado)
        None -> erro na operação
    """

    def __init__(self):
        """
        Inicializa a conexão com o banco de dados.
        """
        self.conn = ConnectDatabase()
        self.conn.conectar()

    def insert_address(self, rua: str, bairro: str, cidade: str, numero: str) -> int | None:
        """
        Insere um novo endereço na tabela `enderecos`.

        Args:
            rua (str): Nome da rua.
            bairro (str): Bairro do endereço.
            cidade (str): Cidade do endereço.
            numero (str): Número do endereço.

        Returns:
            int: ID do endereço inserido.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO enderecos (rua, bairro, cidade, numero)
            VALUES (%s, %s, %s, %s)
            RETURNING endereco_id;
        """
        address: tuple = (rua, bairro, cidade, numero)
        return self.conn.insert(sql_insert, address)

    def insert_people(
        self,
        endereco_id: int,
        nome: str,
        telefone: str,
        n_inscricao_tributaria: str,
        data_nascimento: date
    ) -> int | None:
        """
        Insere uma pessoa na tabela `pessoas`.

        Args:
            endereco_id (int): ID do endereço associado.
            nome (str): Nome da pessoa.
            telefone (str): Telefone.
            n_inscricao_tributaria (str): Número de inscrição tributária.
            data_nascimento (date): Data de nascimento.

        Returns:
            int: ID da pessoa inserida.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO pessoas (endereco_id, nome, telefone, n_inscricao_tributaria, data_nascimento)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING pessoa_id;
        """
        people: tuple = (endereco_id, nome, telefone, n_inscricao_tributaria, data_nascimento)
        return self.conn.insert(sql_insert, people)

    def insert_user(self, email: str, senha: str, tipo_usuario: str) -> int | None:
        """
        Insere um usuário na tabela `usuarios`.

        Args:
            email (str): Email do usuário.
            senha (str): Senha do usuário.
            tipo_usuario (str): Tipo do usuário (ex: admin, comum).

        Returns:
            int: ID do usuário inserido.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO usuarios (email, senha, tipo_usuario)
            VALUES (%s, %s, %s)
            RETURNING usuario_id;
        """
        user: tuple = (email, senha, tipo_usuario)
        return self.conn.insert(sql_insert, user)

    def insert_accuser(self, pessoa_id: int, usuario_id: int | None) -> int | None:
        """
        Insere um acusador na tabela `acusadores`.

        Args:
            pessoa_id (int): ID da pessoa associada.
            usuario_id (int | None): ID do usuário (opcional).

        Returns:
            int: ID do acusador inserido.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO acusadores (pessoa_id, usuario_id)
            VALUES (%s, %s)
            RETURNING acusador_id;
        """
        accuser: tuple = (pessoa_id, usuario_id)
        return self.conn.insert(sql_insert, accuser)

    def insert_accused(self, pessoa_id: int) -> int | None:
        """
        Insere um acusado na tabela `acusados`.

        Args:
            pessoa_id (int): ID da pessoa associada.

        Returns:
            int: ID do acusado inserido.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO acusados (pessoa_id)
            VALUES (%s)
            RETURNING acusado_id;
        """
        accused: tuple = (pessoa_id,)
        return self.conn.insert(sql_insert, accused)

    def insert_mediator(self, pessoa_id: int, usuario_id: int | None, prefeitura_id: int, status_mediador: str) -> int | None:
        """
        Insere um mediador na tabela `mediadores`.

        Args:
            pessoa_id (int): ID da pessoa.
            usuario_id (int): ID do usuário.
            prefeitura_id (int): ID da prefeitura.
            status_mediador (str): Status do mediador.

        Returns:
            int: ID do mediador inserido.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO mediadores (pessoa_id, usuario_id, prefeitura_id, status_mediador)
            VALUES (%s, %s, %s, %s)
            RETURNING mediador_id;
        """
        mediator: tuple = (pessoa_id, usuario_id, prefeitura_id, status_mediador)
        return self.conn.insert(sql_insert, mediator)

    def insert_manager(self, pessoa_id: int, usuario_id: int, prefeitura_id: int, status_gestor: str) -> int | None:
        """
        Insere um gestor na tabela `gestores`.

        Args:
            pessoa_id (int): ID da pessoa.
            usuario_id (int): ID do usuário.
            prefeitura_id (int): ID da prefeitura.
            status_gestor (str): Status do gestor.

        Returns:
            int: ID do gestor inserido.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO gestores(prefeitura_id, usuario_id, pessoa_id, status_gestor)
            VALUES (%s, %s, %s, %s)
            RETURNING gestor_id;
        """
        gestor: tuple = (prefeitura_id, usuario_id, pessoa_id, status_gestor)
        return self.conn.insert(sql_insert, gestor)

    def insert_complaint(
        self,
        audiencia_id: int | None,
        acusador_id: int,
        acusado_id: int,
        causa_denuncia: str,
        detalhamento: str,
        data: date
    ) -> int | None:
        """
        Insere uma denúncia na tabela `denuncias`.

        Args:
            audiencia_id (int | None): ID da audiência (opcional).
            acusador_id (int): ID do acusador.
            acusado_id (int): ID do acusado.
            causa_denuncia (str): Motivo da denúncia.
            detalhamento (str): Descrição detalhada.
            data (date): Data da denúncia.

        Returns:
            int: ID da denúncia inserida.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO denuncias (audiencia_id, acusador_id, acusado_id, causa_denuncia, detalhamento, data_denuncia)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING denuncia_id;
        """
        complaint: tuple = (
            audiencia_id,
            acusador_id,
            acusado_id,
            causa_denuncia,
            detalhamento,
            data,
        )
        return self.conn.insert(sql_insert, complaint)

    def insert_audience(self, mediador_id: int, endereco_id: int, status_audiencia: str, data: date) -> int | None:
        """
        Insere uma audiência na tabela `audiencias`.

        Args:
            mediador_id (int): ID do mediador.
            endereco_id (int): ID do endereço.
            status_audiencia (str): Status da audiência.
            data (date): Data da audiência.

        Returns:
            int: ID da audiência inserida.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO audiencias (mediador_id, endereco_id, status_audiencia, data_audiencia)
            VALUES (%s, %s, %s, %s)
            RETURNING audiencia_id;
        """
        audience: tuple = (mediador_id, endereco_id, status_audiencia, data)
        return self.conn.insert(sql_insert, audience)

    def insert_agreement(self, audiencia_id: int, status_acordo: str, data_acordo: date) -> int | None:
        """
        Insere um acordo na tabela `acordos`.

        Args:
            audiencia_id (int): ID da audiência.
            status_acordo (str): Status do acordo.
            data_acordo (date): Data do acordo.

        Returns:
            int: ID do acordo inserido.
            None: Em caso de erro.
        """
        sql_insert: str = """
            INSERT INTO acordos (audiencia_id, status_acordo, data_acordo)
            VALUES (%s, %s, %s)
            RETURNING acordo_id;
        """
        agreement: tuple = (audiencia_id, status_acordo, data_acordo)
        return self.conn.insert(sql_insert, agreement)


    def insert_cityhall(self, endereco_id: int, cnpj:str) -> int | None:
        sql_insert: str = """
            INSERT INTO prefeituras (endereco_id, cnpj)
            VALUES (%s, %s)
            RETURNING prefeitura_id; 
        """

        cityhall: tuple = (endereco_id, cnpj)
        return self.conn.insert(sql_insert, cityhall)