from typing import Any, Dict, List, Optional, Tuple, Union
from psycopg2 import connect
import toml


class ConnectDatabase:
    def __init__(self, config_path: str = "database/config.toml"):
        self.config_path = config_path

    def conectar(self, user: Optional[str], password: Optional[str]):
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
            print(f"\nErro ao conectar ao banco de dados: {e}")
            raise

    def execute_query(self, query: str, params=None, is_select: bool = False):
        """
        Um método mestre para evitar repetição de código.
        """
        try:
            self.cur.execute(query, params)

            if is_select:
                return self.cur.fetchall()

            self.conn.commit()
            return True
        except Exception as e:
            if self.conn:
                self.conn.rollback()
            print(f"Erro na operação: {e}")
            return None

    def insert(self, query: str, params):
        return self.execute_query(query, params)

    def get(self, query: str, params=None):
        return self.execute_query(query, params, is_select=True)

    def update(self, query, params):
        return self.execute_query(query, params)

    def delete(self, query, params):
        return self.execute_query(query, params)

    def fechar(self):
        """Chame isso SÓ quando não for mais usar o banco."""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Conexão encerrada com segurança.")

    def inicializar_schema(self, schema_path: str = "database/schema.sql") -> None:
        if not self.conn or not self.cur:
            raise ConnectionError(
                "Conexão não estabelecida. Chame conectar() primeiro."
            )

        try:
            with open(schema_path, "r") as f:
                sql_script = f.read()

            self.cur.execute(sql_script)

            self.conn.commit()
            print("Schema executado e alterações salvas.")

        except Exception as e:
            if self.conn:
                self.conn.rollback()
            print(f"Erro ao rodar schema: {e}")
            raise
