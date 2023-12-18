from config import CONN, CURSOR

class Song:
    def __init__ (self,name,albulm):
        self.id=None
        self.name=name
        self.albulm=albulm 

    @classmethod
    def create_table(self):
        sql="""
            CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            albulm TEXT
            )
        """
        CURSOR.execute(sql)

    def save(self):
        sql="""
        INSERT INTO songs(name,albulm) 
        VALUES (?,?)  
        """
        CURSOR.execute(sql,(self.name,self.albulm))
