import mysql.connector
from config.db_config import DB_CONFIG

class PublisherModel:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor()

    def create_publisher(self, name, email, contact_info):
        query = "INSERT INTO publishers (name, email, contact_info) VALUES (%s, %s, %s)"
        values = (name, email, contact_info)
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def delete_publisher(self, publisher_id):
        query = "DELETE FROM publishers WHERE id = %s"
        self.cursor.execute(query, (publisher_id,))
        self.connection.commit()
        return self.cursor.rowcount

    def get_all_publishers(self):
        query = "SELECT * FROM publishers"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()