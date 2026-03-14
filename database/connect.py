from psycopg2 import connect
import psycopg2
class ConnectDatabase:

    def __init__(self):
        # TODO: Os parametros database, user e password, variam de acordo
        # Com a instalacao de cada pessoa do postgres
        
        self.connect = connect(
            database="postgres",
            user="postgres",
            password="3323",
            host="localhost",
            port="5432",
        )

        self.connect.autocommit = True

        self.cur = self.connect.cursor()

    def close(self):
        self.cur.close()
        self.connect.close()
    
    def create_db(self, nome_db: str):
        try:
            sql = f""" CREATE database {nome_db};"""
            self.cur.execute(sql)
            print("criado o banco de dados : {}")
        except psycopg2.errors.DuplicateDatabase:
            print("O banco de dados '{nome_db}', já existe")
