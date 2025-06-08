import mysql.connector
from mysql.connector import Error
from config.sql_config import SQLConfig

class MySQLConnector(SQLConfig):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connection to MySQL database established successfully.")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            self.connection = None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed.")