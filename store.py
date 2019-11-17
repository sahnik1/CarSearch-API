from csv import DictReader
import sqlite3

con = sqlite3.connect("./data.db")
cur = con.cursor()
#cur.execute("CREATE TABLE cars (id INTEGER PRIMARY KEY, year integer, category text, make text, model text);")
#id,Year,Category,Make,Model,No_Of_Recalls,Vehicles_Affected,City_MPG,Highway_MPG,Combined_MPG,Cylinders,Eng_Displ,Transmission,Drive

id = 0
dblister = []
with open('./final.csv','rb') as filein:
    fileinfo = DictReader(filein)
    for row in fileinfo:
        row['id'] = id
        if (row['Year'] == 'NULL'):
            dblister += [(row['id'], None, row['Category'], row['Make'], row['Model'])]
        else:
            dblister += [(row['id'], int(row['Year']), row['Category'], row['Make'], row['Model'])]
        id += 1

cur.execute("SELECT * FROM cars WHERE id = 0 ")
con.commit()
#cur.executemany("INSERT INTO cars (id, year, category, make, model) VALUES (?, ?, ?, ?, ?);", dblister)