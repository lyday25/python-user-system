import sqlite3 as sql
def init2_db():
    connection = sql.connect('data.db')

    with open('schemaa.sql') as f:
       connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO userpost (title, content) VALUES (?, ?)",
            ('The nigeria child is born', 'The birth of the Nigerian child has never celeberated')
            )
    
    cur.execute("INSERT INTO userpost (title, content) VALUES (?, ?)",
            ('Civil war', 'The Nigeria Civil war was fight with no victor no vanaquished')
            )
    cur.execute("INSERT INTO userpost (title, content) VALUES (?, ?)",
            ('Hunger in the land ', 'There is seriouse hunger in the land of Nigeria currently since the advent of this new president')
            )



        
    connection.commit()
    connection.close()
    print('Recoords posted into the database.')
        
init2_db()     
        
      