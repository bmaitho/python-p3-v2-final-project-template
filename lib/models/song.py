from models.__init__ import CURSOR, CONN
from models.artist import Artist

class Song:
    all = {}

    def __init__(self, title, artist_id, genre_id, id=None):
        self.id = id
        self.title = title
        self.artist_id = artist_id
        self.genre_id = genre_id

    def __repr__(self):
        return f"<Song(title={self.title}, artist_id={self.artist_id}, genre_id={self.genre_id}, id={self.id})>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def artist_id(self):
        return self._artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        if isinstance(artist_id, int) and artist_id > 0:
            self._artist_id = artist_id
        else:
            raise ValueError("Artist ID must be a positive integer")

    @property
    def genre_id(self):
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        if isinstance(genre_id, int) and genre_id > 0:
            self._genre_id = genre_id
        else:
            raise ValueError("Genre ID must be a positive integer")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Song instances """
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            title TEXT,
            artist_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id),
            FOREIGN KEY (genre_id) REFERENCES genres(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Song instances """
        sql = """
            DROP TABLE IF EXISTS songs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the attributes of the current Song instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO songs (title, artist_id, genre_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.artist_id, self.genre_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, artist_id, genre_id):
        """ Initialize a new Song instance and save the object to the database """
        song = cls(title, artist_id, genre_id)
        song.save()
        return song

    def update(self):
        """Update the table row corresponding to the current Song instance."""
        sql = """
            UPDATE songs
            SET title = ?, artist_id = ?, genre_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.artist_id, self.genre_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Song instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM songs
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def get_all(cls):
        """Return a list containing a Song object per row in the table"""
        sql = """
            SELECT *
            FROM songs
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Song object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM songs
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return a Song object corresponding to the table row matching the specified title"""
        sql = """
            SELECT *
            FROM songs
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        """Create a Song instance from a database row"""
        id, title, artist_id, genre_id = row
        return cls(title, artist_id, genre_id, id)
