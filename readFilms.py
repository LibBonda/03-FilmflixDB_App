from connect import *
  
def read_tblFilms():
    try:  # select all records from the table
       
        rows = dbCursor.execute("SELECT * FROM tblFilms").fetchall()
  
        if not rows: # row is the record returned based on the specific filmID
            print(f"No record(s) exists")
        # loop through all the records in the row variable
        else:
            for aRecord in rows:
                # print all record
                print(aRecord)
    except sql.connect.OperationalError as e:
        print(f"Records not found: {e}")
if __name__ == "__main__":
    read_tblFilms()
    
   