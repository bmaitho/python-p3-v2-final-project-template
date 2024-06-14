from models.__init__ import CURSOR, CONN

class Genre:
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
    def create_genre(cls):  
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
         
        
    
    
