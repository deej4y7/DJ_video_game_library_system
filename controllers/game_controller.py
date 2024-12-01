from models.game_model import GameModel

class GameController:
    def __init__(self):
        self.game_model = GameModel()

    def add_game(self, title, genre_id, developer_id, publisher_id, release_date, description):
        return self.game_model.create_game(title, genre_id, developer_id, publisher_id, release_date, description)

    def get_all_games(self):
        return self.game_model.get_all_games()

    def get_game_by_id(self, game_id):
        return self.game_model.get_game_by_id(game_id)

    def update_game(self, game_id, title, genre_id, developer_id, publisher_id, release_date, description):
        return self.game_model.update_game(game_id, title, genre_id, developer_id, publisher_id, release_date, description)

    def delete_game(self, game_id):
        return self.game_model.delete_game(game_id)

    def get_games_by_genre(self, genre_id):
        return self.game_model.get_games_by_genre(genre_id)