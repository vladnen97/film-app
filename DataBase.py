import sqlite3

class Database():
    bdname = 'filmdb.db'
    def __init__(self):
        self.con=sqlite3.connect(self.bdname)
        self.cur= self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS genres(
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genres_name TEXT NOT NULL, UNIQUE (genres_name))""")
        
        self.cur.execute("""CREATE TABLE IF NOT EXISTS
                    films(
                    title TEXT NOT NULL,
                    genre1_id INTEGER NOT NULL,
                    genre2_id INTEGER NOT NULL,
                    year INTEGER NOT NULL,
                    PRIMARY KEY(title, year),
                    FOREIGN KEY (genre1_id) REFERENCES genres(genre_id),
                    FOREIGN KEY (genre2_id) REFERENCES genres(genre_id)
                    )""")

        self.con.commit()

    class MyTuple:
        def __init__(self, value):
            self.value=value

        def __str__(self):
            return self.value[1]
        

    def get_all_genres(self):
        result = list()
        for i in self.cur.execute("""SELECT * FROM genres"""):
            result.append(self.MyTuple(i))
        return result

        
    def get_ganreid_by_name(self, genre):
        if not self.cur.execute(f"""SELECT genre_id FROM genres WHERE genres_name ='{genre}'""").fetchone():
            self.cur.execute(f"""INSERT INTO genres(genres_name) VALUES('{genre}')""")
        return self.cur.execute(f"""SELECT genre_id FROM genres WHERE genres_name ='{genre}'""").fetchone()[0]

    def append(self, name, genre1, genre2, year):
        if name != '' and genre1 !='' and genre2 != '' and year !='':
            name = name.lower()
            genre1 = genre1.lower()
            genre2 = genre2.lower()
            year = year.lower()
 
            genre1_id = self.get_ganreid_by_name(genre1)
            genre2_id = self.get_ganreid_by_name(genre2)
            
            self.cur.execute(f"""INSERT INTO films VALUES(
                    '{name}', {genre1_id}, {genre2_id}, {year})""")
            
            self.con.commit()
            return True   
        else:
            return False

    def delete(self, name, year):
        if name !='' and year !='':
            self.cur.execute(f"""DELETE FROM films WHERE
                                title = '{name}' and year = {year}""")
            self.con.commit()
            return True
        else:
            return False

    def poisk(self, genre1, genre2, yearot, yeardo):
        genre1 = genre1.lower()
        genre2 = genre2.lower()
        esli1 ="(genre1= '{genre1}'or genre1='{genre2}')and "
        esli2 = "(genre2= '{genre2}' or genre2='{genre1}')and "
        if genre1 == '':
            esli=''
        if genre2== '':
            esli2=''
        if yearot =='' or (not yearot.isdigit()):
            yearot = str(0)
        if yeardo=='' or (not yeardo.isdigit()):
            yeardo=str(9999)
            
        result =  self.cur.execute(f"""SELECT * FROM films WHERE
                        {esli}
                        {esli2}
                        (year >= {yearot} and year<= {yeardo}) ORDER BY title""")
        self.con.commit()
        
        return result


    

    
        
        
                    
            
        
        
