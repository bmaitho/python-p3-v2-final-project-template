from models.__init__ import CURSOR, CONN

class Genre:
    all = {}
    def __init__(self, name,id=None, ):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"<Genre(name={self.name}, id={self.id})"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):

        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    @classmethod
    def create_table(cls):  
         """ Create a new table to persist the attributes of Genre instances """
         sql = """
            CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
         CURSOR.execute(sql)
         CONN.commit()
    def drop_table(cls):  
         """ Drop the table that persists Genres instances """
         sql =  """
            DROP TABLE IF EXISTS genres;
        """
            
         CURSOR.execute(sql)
         CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Genre instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO genres (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def create(cls, name):
        """ Initialize a new Genre instance and save the object to the database """
        genre = cls(name)
        genre.save()
        return genre     
        
    def delete(self):
        """Delete the table row corresponding to the current Genre instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM genres
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def get_all(cls):
        """Return a list containing a Genre object per row in the table"""
        sql = """
            SELECT *
            FROM genres
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
