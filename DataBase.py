import sqlite3

class Database():
    bdname = 'filmdb.db'
    def __init__(self):
        self.con=sqlite3.connect(self.bdname)
        self.cur= self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS
                    films(
                    title TEXT NOT NULL,
                    genre1 TEXT NOT NULL,
                    genre2 TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    PRIMARY KEY(title, year))
                    """)

        self.con.commit()

    def append(self, name, genre1, genre2, year):
        if name != '' and genre1 !='' and genre2 != '' and year !='':
            name = name.lower()
            genre1 = genre1.lower()
            genre2 = genre2.lower()
            year = year.lower()
            self.cur.execute(f"""INSERT INTO films VALUES(
                            '{name}', '{genre1}', '{genre2}', {year})""")
            
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


    

    
        
        
                    
            
        
        
