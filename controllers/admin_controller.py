# admin_controller.py

from models.user_model import UserModel
from models.game_model import GameModel
from models.genre_model import GenreModel
from models.developer_model import DeveloperModel
from models.publisher_model import PublisherModel

class AdminController:
    def __init__(self):
        self.user_model = UserModel()
        self.game_model = GameModel()
        self.genre_model = GenreModel()
        self.developer_model = DeveloperModel()
        self.publisher_model = PublisherModel()

    def add_user(self, first_name, last_name, username, email, password, roles):
        return self.user_model.create_user(first_name, last_name, username, email, password, roles)

    def remove_user(self, user_id):
        return self.user_model.delete_user(user_id)

    def update_user(self, user_id, first_name=None, last_name=None, username=None, email=None, password=None, roles=None):
        return self.user_model.update_user(user_id, first_name, last_name, username, email, password, roles)

    def list_users(self):
        return self.user_model.get_all_users()

    def add_game(self, title, release_date, developer_id, publisher_id, file_size, is_featured):
        return self.game_model.create_game(title, release_date, developer_id, publisher_id, file_size, is_featured)

    def remove_game(self, game_id):
        return self.game_model.delete_game(game_id)

    def update_game(self, game_id, title=None, release_date=None, developer_id=None, publisher_id=None, file_size=None, is_featured=None):
        return self.game_model.update_game(game_id, title, release_date, developer_id, publisher_id, file_size, is_featured)

    def list_games(self):
        return self.game_model.get_all_games()

    def add_genre(self, genre_name):
        return self.genre_model.create_genre(genre_name)

    def remove_genre(self, genre_id):
        return self.genre_model.delete_genre(genre_id)

    def list_genres(self):
        return self.genre_model.get_all_genres()

    def add_developer(self, name, email, contact_info):
        return self.developer_model.create_developer(name, email, contact_info)

    def remove_developer(self, developer_id):
        return self.developer_model.delete_developer(developer_id)

    def list_developers(self):
        return self.developer_model.get_all_developers()

    def add_publisher(self, name, email, contact_info):
        return self.publisher_model.create_publisher(name, email, contact_info)

    def remove_publisher(self, publisher_id):
        return self.publisher_model.delete_publisher(publisher_id)

    def list_publishers(self):
        return self.publisher_model.get_all_publishers()