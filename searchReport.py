from connect import *
import logging
import time

filename = __file__

logging.basicConfig(filename=r"FilmsDBFile.log", format='[%(filename)s:%(lineno)d in function %(funcName)s]', level=logging.DEBUG,)

# create a subroutine
def search():
    try:
        field = input("Would you like to search by filmID, title, yearReleased, rating, duration or genre: ")
        if field == "filmID":
            idInput = int(input("Enter filmID: "))
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idInput}")
            row = dbCursor.fetchone()
            if row == None:
                print(f"No record with {idInput} exists in the table: ")
                logging.warning(f"On {time.asctime()}, file is {filename}, user entered {idInput} as {field}")
            else:
                for aRecord in row:
                    print(aRecord)
        elif field == "duration":
            lower_duration = int(input("Enter minimum duration (in minutes): "))
            upper_duration = int(input("Enter maximum duration (in minutes): "))
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE duration BETWEEN {lower_duration} AND {upper_duration}")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No records found with duration between {lower_duration} and {upper_duration} minutes.")
            else:
                for records in rows:
                    print(records)
        elif field in ["title", "yearReleased", "rating", "genre"]:
            searchInput = input(f"Enter search field for  {field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{searchInput}%'")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with field {field} matching '{searchInput}' in the table.")
            else:
                for records in rows:
                    print(records)
        else:
            print(f"Invalid search field {field}")
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")

if __name__ == "__main__":
    search()