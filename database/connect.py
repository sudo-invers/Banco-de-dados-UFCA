import psycopg2
class ConnectDatabase:

    def __init__(self):
        self.connect = psycopg2.connect(
            database="sgcc",
            host="localhost",
            user="admin",
            password=" ",
            port="5432"
        )

        self.cur = self.connect.cursor()

    def close(self):
        self.cur.close()
        self.connect.close()