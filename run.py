# Author: Karanjot Singh Sahni
# Description: Web Api using Flask/Python for Aggregated Data from Previous CarSearch Project

from flask import Flask
from flask_restful import Resource, Api

import sqlite3
import json

app = Flask(__name__)
api = Api(app)

class IdSearch(Resource):
    def get(self, carid):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM cars WHERE id=?;", [carid])
        con.commit()
        result = cur.fetchall()
        if (result is None):
            return { 'Status' : 'No Content' }, 204

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in result]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        #jsontemp = {'ID' : result[0], 'Year' : str(result[1]), 'Make' :  str(result[3]), 'Model' :  str(result[4]), 'Category' :  str(result[2])}
        return { 'Status' : 'Success', 'Data': datajson}, 200

class YearList(Resource):
    def get(self, year):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM cars WHERE year=?;", [year])
        con.commit()
        results = cur.fetchall()

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in results]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        return { 'Status' : 'Success', 'Records_Found' : len(datajson), 'Data' : datajson }, 200

class ComboList(Resource):
    def get(self, year, make, model):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        if (model.lower() == 'any'):
            cur.execute("SELECT * FROM cars WHERE year=:year AND make LIKE :make AND model LIKE :model;", {'year' : int(year), 'make' : '%'+(make.upper())+'%', 'model' : '%'})
        else:
            cur.execute("SELECT * FROM cars WHERE year=:year AND make LIKE :make AND model LIKE :model;", {'year' : int(year), 'make' : '%'+(make.upper())+'%', 'model' : '%'+(model.upper())+'%'})
        
        #con.commit()
        results = cur.fetchall()

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in results]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        return { 'Status' : 'Success', 'Year' : year, 'Make' : make, 'Model' : model, 'Records_Found' : len(datajson), 'Data' : datajson }, 200

api.add_resource(IdSearch, '/cars/id=<int:carid>')
api.add_resource(YearList, '/cars/year=<int:year>')
api.add_resource(ComboList, '/cars/year=<int:year>,make=<string:make>,model=<string:model>')

if __name__ == '__main__':
    app.run(debug=True)