from csv import DictReader
import sqlite3

con = sqlite3.connect("./data.db")
cur = con.cursor()
cur.execute("CREATE TABLE cars (id INTEGER PRIMARY KEY, year integer, category text, make text, model text, No_Of_Recalls integer,Vehicles_Affected integer,City_MPG integer,Highway_MPG integer,Combined_MPG integer,Cylinders integer,Eng_Displ real,Transmission text,Drive text);")
#id,Year,Category,Make,Model,No_Of_Recalls,Vehicles_Affected,City_MPG,Highway_MPG,Combined_MPG,Cylinders,Eng_Displ,Transmission,Drive

id = 0
dblister = []
intkeys = ['Year', 'No_Of_Recalls','Vehicles_Affected','City_MPG','Highway_MPG','Combined_MPG','Cylinders']
allkeys = ['id','Year','Category','Make','Model','No_Of_Recalls','Vehicles_Affected','City_MPG','Highway_MPG','Combined_MPG','Cylinders','Eng_Displ','Transmission','Drive']
with open('./final.csv','rb') as filein:
    fileinfo = DictReader(filein)
    for row in fileinfo:
        templist = []
        for key in allkeys:
            if (row[key] == 'NULL'):
                templist += [0]
            elif (key == 'id'):
                templist += [id]
            else:
                if (key in intkeys):
                    templist += [int(row[key])]
                elif (key == 'Eng_Displ'):
                    templist += [float(row[key])]
                else:
                    templist += [row[key].upper()]
        dblister += [tuple(templist)]
        id += 1
#cur.execute("SELECT * FROM cars WHERE id = 0 ")
cur.executemany("INSERT INTO cars (id, year, category, make, model,No_Of_Recalls,Vehicles_Affected,City_MPG,Highway_MPG,Combined_MPG,Cylinders,Eng_Displ,Transmission,Drive) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", dblister)
con.commit()