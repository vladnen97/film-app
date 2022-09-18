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
        
    def update_genre_table(self, genre, add_or_del):
        genre = genre.lower()
        
        if add_or_del:
            self.cur.execute(f"""INSERT INTO genres(genres_name) VALUES('{genre}')""")
        else:
            self.cur.execute(f"""DELETE FROM genres WHERE genres_name = '{genre}' """)
            
        self.con.commit()
        
    def get_all_genres(self):
        result = list()
        for i in self.cur.execute("""SELECT * FROM genres"""):
            result.append(self.MyTuple(i))
            
        self.con.commit()
        return result

    def append(self, name, genre1, genre2, year):
        if name != '' and genre1 !='' and genre2 != '' and year !='':
            name = name.lower()
            
            self.cur.execute(f"""INSERT INTO films VALUES(
                    '{name}', {genre1}, {genre2}, {year})""")
            
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
        
        esli1 ="(g1.genres_name = 'боевик' or g1.genres_name = 'триллер') and"
        esli2 = "(g2.genres_name = 'триллер' or g2.genres_name = 'боевик') and"
        if genre1 == '':
            esli=''
        if genre2== '':
            esli2=''
        if yearot =='' or (not yearot.isdigit()):
            yearot = str(0)
        if yeardo=='' or (not yeardo.isdigit()):
            yeardo=str(9999)
            
        result =  self.cur.execute(f"""SELECT films.title, g1.genres_name, g2.genres_name, films.year
                        FROM films INNER JOIN genres as g1
                            ON films.genre1_id = g1.genre_id
                        INNER JOIN genres as g2
                            ON films.genre2_id = g2.genre_id
                        WHERE
                        {esli1}
                        {esli2}
                        (year >= {yearot} and year<= {yeardo}) ORDER BY title""")
        self.con.commit()
        
        return result


    

    
        
        
                    
            
        
        
