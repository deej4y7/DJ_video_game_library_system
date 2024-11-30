from models.user_model import UserModel

class AuthController:
    def __init__(self):
        self.user_model = UserModel()

    def register_user(self, first_name, last_name, username, email, password, roles):
        return self.user_model.create_user(first_name, last_name, username, email, password, roles)

    def login_user(self, username, password):
        user = self.user_model.get_user_by_username(username)

        if user and user[5] == password:
            return {"status": "success", "user_id": user[0], "roles": user[6]}
        else:
            return {"status": "error", "message": "Invalid username or password"}

    def get_user_info(self, user_id):
        return self.user_model.get_user_by_id(user_id)