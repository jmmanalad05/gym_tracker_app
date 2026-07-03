import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self, app=None):
        self.app = app
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return self.conn

    def get_connection(self):
        if not self.conn or not self.conn.is_connected():
            return self.connect()
        return self.conn