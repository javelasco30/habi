import mysql.connector

from sqlite3 import Cursor
from config import DATABASE_CONFIG


class ConnectorDB():

    def __init__(self):
        self.host = DATABASE_CONFIG['db_host']
        self.user = DATABASE_CONFIG['db_user']
        self.port = DATABASE_CONFIG['db_port']
        self.password = DATABASE_CONFIG['db_password']
        self.database = DATABASE_CONFIG['db_name']

    def connect(self):
        conn = mysql.connector.connect(host=self.host, port=self.port,
                                       user=self.user, password=self.password,
                                       database=self.database)
        return conn

    def dictfetchall(self, description, fetchall):
        return [
            dict(zip([col[0] for col in description], row))
            for row in fetchall
           ]

    def execute_sql(self, sql, params):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        fetchall = self.dictfetchall(cursor.description, cursor.fetchall())
        conn.close()
        return fetchall
