from psycopg2 import connect
import toml


class ConnectDatabase:
    def __init__(self, user=None, password=None):
        # Os parametros database, user e password, variam de acordo
        # Com a instalacao de cada pessoa do postgres
        config = toml.load("database/config.toml")["database"]
        self.user = user or config["user"]
        self.password = password or config["password"]
        self.connect = connect(
            database=config["database"],
            user=self.user,
            password=self.password,
            host=config["host"],
            port=config["port"],
        )

        self.cur = self.connect.cursor()

    def close(self):
        self.cur.close()
        self.connect.close()

    # def create_db(self, nome_db: str):
    #    try:
    #        sql = f""" CREATE database {nome_db};"""
    #        self.cur.execute(sql)
    #        print("criado o banco de dados : {}")
    #    except psycopg2.errors.DuplicateDatabase:
    #        print("O banco de dados '{nome_db}', já existe")
