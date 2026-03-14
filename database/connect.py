from psycopg2 import connect
class ConnectDatabase:

    def __init__(self):
        self.connect = connect(
            database="sgcc",
            host="localhost",
            user="admin",
            password="admin",
            port="5432"
        )

        self.cur = self.connect.cursor()

    def close(self):
        self.cur.close()
        self.connect.close()