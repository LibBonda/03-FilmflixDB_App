from connect import *
import datetime

# Create a table if it doesn't exist
dbCursor.execute('''
    CREATE TABLE IF NOT EXISTS tblfilms (
        filmID INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        yearReleased INTEGER,
        rating TEXT,
        duration REAL,
        genre TEXTOne
    )
''')

# create a subroutine
def insert_tblFilms():
    # create an empty list
    tblFilms = []
    
    # ask for user input (title, yearReleased, rating, duration, or genre)
    title = input("Enter Film Title: ")
    yearReleased = int(input("Enter Year: "))
    rating = input("Enter Rating: ")
    duration = int(input("Enter Time Duration: "))
    genre = input("Enter Genre: ")
    
    print(f"Data: {title, yearReleased, rating, duration, genre}")
    
    # append data title, yearReleased, rating, duration, genre
    tblFilms.extend([title, yearReleased, rating, duration, genre])
    print(f"The films list {tblFilms}")

    try:
        # Using placeholders to prevent SQL injection
        # Values directly from the list
        dbCursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)", tblFilms)
        dbCon.commit()  # make the changes permanent
        print("Film inserted in the Table")
    except sql.OperationalError as e:
        # dbCon.rollback()
        print(f"Insert failed {e}")

if __name__ == "__main__":
    insert_tblFilms()
