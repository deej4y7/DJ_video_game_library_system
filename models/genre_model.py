class GenreModel:
    def __init__(self, db):
        self.db = db

    def add_genre(self, genre_name):
        query = """
            INSERT INTO genres (genre_name) 
            VALUES (%s)
        """
        self.db.execute_query(query, (genre_name,))

    def update_genre(self, genre_id, genre_name):
        query = "UPDATE genres SET genre_name = %s WHERE id = %s"
        self.db.execute_query(query, (genre_name, genre_id))

    def delete_genre(self, genre_id):
        try:
            query = "DELETE FROM genres WHERE id = %s"
            self.db.execute_query(query, (genre_id,))
            print(f"Genre with ID {genre_id} has been deleted.")
        except Exception as e:
            print(f"Error deleting genre: {e}")

    def get_genre(self, genre_id):
        query = "SELECT * FROM genres WHERE id = %s"
        return self.db.fetch_one(query, (genre_id,))

    def get_all_genres(self):
        query = "SELECT * FROM genres"
        return self.db.fetch_all(query)