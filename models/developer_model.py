import mysql.connector
from config.db_config import DB_CONFIG

class DeveloperModel:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor()

    def create_developer(self, name, email, contact_info):
        query = "INSERT INTO developers (name, email, contact_info) VALUES (%s, %s, %s)"
        values = (name, email, contact_info)
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def delete_developer(self, developer_id):
        query = "DELETE FROM developers WHERE id = %s"
        self.cursor.execute(query, (developer_id,))
        self.connection.commit()
        return self.cursor.rowcount

    def get_all_developers(self):
        query = "SELECT * FROM developers"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()