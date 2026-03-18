import sys
from psycopg2 import connect
import toml


class ConnectDatabase:
    def __init__(self, config_path: str = "database/config.toml") -> None:
        """
        Inicializa a classe de conexão com o banco de dados.

        Args:
            config_path (str): Caminho para o arquivo de configuração TOML.
        """
        self.config_path = config_path
        self.cur = None
        self.conn = None

    def conectar(self, user: str | None = None, password: str | None = None) -> None:
        """
        Estabelece conexão com o banco de dados PostgreSQL.

        Caso `user` e `password` não sejam informados, utiliza os valores
        definidos no arquivo de configuração.

        Args:
            user (str | None): Usuário do banco.
            password (str | None): Senha do banco.

        Raises:
            Exception: Caso ocorra erro ao conectar ao banco.
        """
        try:
            config = toml.load(self.config_path)["database"]

            user = user or config["user"]
            password = password or config["password"]

            self.conn = connect(
                database=config["database"],
                user=user,
                password=password,
                host=config["host"],
                port=config["port"],
            )
            self.cur = self.conn.cursor()
            print("Conexão estabelecida com sucesso.")

        except Exception as e:
            print(f"\nErro ao conectar ao banco de dados: {e}", file=sys.stderr)
            raise

    def execute_query(self, query: str, params: tuple | None, is_select: bool = False, is_insert: bool = False) -> list[tuple] | int | bool | None:
        """
        Executa uma query SQL genérica.

        Este método centraliza a execução de queries, evitando repetição
        de código para operações CRUD.

        Args:
            query (str): Query SQL a ser executada.
            params (tuple | None): Parâmetros da query.
            is_select (bool): Indica se a query é um SELECT.
            is_insert (bool): Indica se a query é um INSERT.

        Returns:
            list[tuple]: Resultado da consulta (se SELECT).
            int: RETURNING da entidade (se INSERT) - usado para recuperar o id.
            bool: True se operação de escrita for bem-sucedida.
            None: Em caso de erro.
        """
        try:
            self.cur.execute(query, params)

            if is_select:
                result: list[tuple] = self.cur.fetchall()
                return result

            if is_insert:
                result: tuple = self.cur.fetchone()
                self.conn.commit()
                entity_returning: int | None = result[0] if result else None
                return entity_returning


            self.conn.commit()
            return True

        except Exception as e:
            if self.conn:
                self.conn.rollback()
            print(f"Erro na operação: {e}", file=sys.stderr)
            return None

    def insert(self, query: str, params: tuple) -> int | None:
        """
        Executa uma operação de INSERT.

        Args:
            query (str): Query SQL de inserção.
            params (tuple): Parâmetros da query.

        Returns:
            int: ID gerado para entidade.
            None: Em caso de erro.
        """
        return self.execute_query(query, params, is_insert=True)

    def get(self, query: str, params: tuple | None = None) -> list[tuple] | None:
        """
        Executa uma operação SELECT.

        Args:
            query (str): Query SQL de consulta.
            params (tuple | None): Parâmetros da query.

        Returns:
            list[tuple]: Lista de resultados.
            None: Em caso de erro.
        """
        return self.execute_query(query, params, is_select=True)

    def update(self, query: str, params: tuple) -> bool | None:
        """
        Executa uma operação de UPDATE.

        Args:
            query (str): Query SQL de atualização.
            params (tuple): Parâmetros da query.

        Returns:
            bool: True se sucesso.
            None: Em caso de erro.
        """
        return self.execute_query(query, params)

    def delete(self, query: str, params: tuple) -> bool | None:
        """
        Executa uma operação de DELETE.

        Args:
            query (str): Query SQL de remoção.
            params (tuple): Parâmetros da query.

        Returns:
            bool: True se sucesso.
            None: Em caso de erro.
        """
        return self.execute_query(query, params)

    def fechar(self) -> None:
        """
        Fecha a conexão com o banco de dados.

        Deve ser chamado quando não houver mais necessidade de uso da conexão.
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Conexão encerrada com segurança.")

    def inicializar_schema(self, schema_path: str = "database/schema.sql") -> None:
        """
        Executa um script SQL para inicializar o schema do banco.

        Args:
            schema_path (str): Caminho para o arquivo SQL.
        """
        with open(schema_path, "r") as f:
            sql_script: str = f.read()

        self.cur.execute(sql_script)
        self.conn.commit()
        print("Schema executado e alterações salvas.")