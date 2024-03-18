# User_management_System
This is user management system web based Flask Application with an Sql database
first create directory user_management_system
$ cd user_management_system
# now try to vreate a virtua; environment
$python3 -m venv venv
# now activate the virtauol eneviorment

$ Source venev/bin/activate
# now create the the schema.sql to house the table creation for the projects
$ vi scheme.sql
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  content TEXT NOT NULL
  
);

Now create another file to the initail db set upp

$ vi init_db.py

import sqlite3 as sql
def init_db():
    connection = sql.connect('database.db')


    with open('schema.sql') as f:
        connection.executescript(f.read())

        cur = connection.cursor()
        
        connection.commit()
        connection.close()
        print('Initialized the database.')
        
init_db()  


#Immediately this is done it creates the database.db in the target root directory

#Now we now need toi install the Flask web framework using the cokmand below


$pip install flask
        


