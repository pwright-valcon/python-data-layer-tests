from dao.interfaces.example_dao import ExampleDAO
import psycopg2


class ExampleDAORDS(ExampleDAO):
    def __init__(self, db_config):
        self.db_connection = psycopg2.connect(**db_config)

    def select_one(self):
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('SELECT 1;')
            return cursor.fetchall()
        finally:
            cursor.close()
            self.db_connection.close()
