import sqlite3 as sql # import the standard sqlite3 module

import os
mypassword = os.environ.get('PythonVSCode')

try:
    # use the module, start by creating db connection(variable to hold the folder/file)
    # using the connect function from sqlite3 module.
    with sql.connect("FilmflixDB/filmflix.db") as dbCon:
        # once the connection and/or dbfile is created
        # create a cursor object(variable) and call it cursor method
        dbCursor = dbCon.cursor() # use to execute sql statements
        
except sql.OperationalError as e: # flag sql error
    # handle the exception/error raised
    print(f"Connection failed: {e}")
    
    
    

   