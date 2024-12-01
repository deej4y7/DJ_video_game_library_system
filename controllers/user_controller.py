from models.user_model import UserModel

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def register_user(self, first_name, last_name, username, email, password, roles):
        return self.user_model.create_user(first_name, last_name, username, email, password, roles)

    def login_user(self, username, password):
        return self.user_model.get_user_by_username(username, password)

    def get_user_info(self, user_id):
        return self.user_model.get_user_by_id(user_id)

    def update_user(self, user_id, first_name=None, last_name=None, email=None, password=None, roles=None):
        return self.user_model.update_user(user_id, first_name, last_name, email, password, roles)

    def delete_user(self, user_id):
        return self.user_model.delete_user(user_id)