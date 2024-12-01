class GameModel:
    def __init__(self, db):
        self.db = db

    def add_game(self, title, release_date, developer_id, publisher_id, file_size, is_featured):
        query = """
            INSERT INTO games (title, release_date, developer_id, publisher_id, file_size, is_featured) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (title, release_date, developer_id, publisher_id, file_size, is_featured))

    def update_game(self, game_id, title=None, release_date=None, developer_id=None, publisher_id=None, file_size=None, is_featured=None):
        query = "UPDATE games SET "
        updates = []
        params = []

        if title is not None:
            updates.append("title = %s")
            params.append(title)

        if release_date is not None:
            updates.append("release_date = %s")
            params.append(release_date)

        if developer_id is not None:
            updates.append("developer_id = %s")
            params.append(developer_id)

        if publisher_id is not None:
            updates.append("publisher_id = %s")
            params.append(publisher_id)

        if file_size is not None:
            updates.append("file_size = %s")
            params.append(file_size)

        if is_featured is not None:
            updates.append("is_featured = %s")
            params.append(is_featured)

        if not updates:
            print("No fields to update.")
            return

        query += ", ".join(updates) + " WHERE id = %s"
        params.append(game_id)

        self.db.execute_query(query, tuple(params))

    def delete_game(self, game_id):
        try:
            query = "DELETE FROM games WHERE id = %s"
            self.db.execute_query(query, (game_id,))
            print(f"Game with ID {game_id} has been deleted.")
        except Exception as e:
            print(f"Error deleting game: {e}")

    def get_game(self, game_id):
        query = "SELECT * FROM games WHERE id = %s"
        return self.db.fetch_one(query, (game_id,))

    def get_all_games(self):
        query = "SELECT * FROM games"
        return self.db.fetch_all(query)

    def get_games_by_genre(self, genre_id):
        query = """
            SELECT g.* FROM games g
            JOIN games_genres gg ON g.id = gg.game_id
            WHERE gg.genre_id = %s
        """
        return self.db.fetch_all(query, (genre_id,))

    def get_games_by_developer(self, developer_id):
        query = "SELECT * FROM games WHERE developer_id = %s"
        return self.db.fetch_all(query, (developer_id,))

    def get_games_by_publisher(self, publisher_id):
        query = "SELECT * FROM games WHERE publisher_id = %s"
        return self.db.fetch_all(query, (publisher_id,))

    def set_featured(self, game_id, is_featured):
        query = "UPDATE games SET is_featured = %s WHERE id = %s"
        return self.db.execute(query, (is_featured, game_id))

    def get_featured_games(self):
        query = "SELECT id FROM games WHERE is_featured = TRUE"
        return self.db.fetch_all(query)