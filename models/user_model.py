from models.database import Database

class UserModel:
    def __init__(self):
        self.db = Database()

    def add_user(self, first_name, last_name, username, email, password):
        query = """
            INSERT INTO users (first_name, last_name, username, email, password, date_joined)
            VALUES (%s, %s, %s, %s, %s, NOW())
        """
        self.db.execute_query(query, (first_name, last_name, username, email, password))

    def authenticate_user(self, username, password):
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        return self.db.fetch_one(query, (username, password))

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        return self.db.fetch_one(query, (user_id,))

    def update_user(self, user_id, first_name=None, last_name=None, email=None, password=None):
        query = "UPDATE users SET "
        updates = []
        params = []

        if first_name is not None:
            updates.append("first_name = %s")
            params.append(first_name)

        if last_name is not None:
            updates.append("last_name = %s")
            params.append(last_name)

        if email is not None:
            updates.append("email = %s")
            params.append(email)

        if password is not None:
            updates.append("password = %s")
            params.append(password)

        if not updates:
            print("No fields to update.")
            return

        query += ", ".join(updates) + " WHERE id = %s"
        params.append(user_id)

        self.db.execute_query(query, tuple(params))

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s"
        self.db.execute_query(query, (user_id,))

    def close(self):
        self.db.close()
