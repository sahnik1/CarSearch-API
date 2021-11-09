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
        if len(result) < 1:
            return { 'Status' : 'No Content' }, 200

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in result]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        #jsontemp = {'ID' : result[0], 'Year' : str(result[1]), 'Make' :  str(result[3]), 'Model' :  str(result[4]), 'Category' :  str(result[2])}
        return { 'Status' : 'Success', 'Records_Found' : len(datajson), 'Data': datajson}, 200

class MakeList(Resource):
    def get(self, make):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM cars WHERE make like ?;", [make])
        con.commit()
        result = cur.fetchall()
        if len(result) < 1:
            return { 'Status' : 'No Content' }, 200

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in result]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        #jsontemp = {'ID' : result[0], 'Year' : str(result[1]), 'Make' :  str(result[3]), 'Model' :  str(result[4]), 'Category' :  str(result[2])}
        return { 'Status' : 'Success', 'Make': make, 'Records_Found': len(datajson), 'Data': datajson}, 200

class ModelList(Resource):
    def get(self, model):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM cars WHERE model like ?;", [model])
        con.commit()
        result = cur.fetchall()
        if len(result) < 1:
            return { 'Status' : 'No Content' }, 200

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in result]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        #jsontemp = {'ID' : result[0], 'Year' : str(result[1]), 'Make' :  str(result[3]), 'Model' :  str(result[4]), 'Category' :  str(result[2])}
        return { 'Status' : 'Success', 'Model': model, 'Records_Found': len(datajson), 'Data': datajson}, 200

class MakeModelList(Resource):
    def get(self, make, model):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM cars WHERE make LIKE :make and model LIKE :model;", {'make' : '%'+(make.upper())+'%', 'model' : '%'+(model.upper())+'%'})
        con.commit()
        
        #con.commit()
        results = cur.fetchall()
        if len(results) < 1:
            return { 'Status' : 'No Content' }, 200

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in results]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        return { 'Status' : 'Success', 'Make' : make, 'Model' : model, 'Records_Found' : len(datajson), 'Data' : datajson }, 200

class YearMakeList(Resource):
    def get(self, year, make):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM cars WHERE year=:year AND make LIKE :make;", {'year' : int(year), 'make' : '%'+(make.upper())+'%'})
        con.commit()
        
        results = cur.fetchall()
        if len(results) < 1:
            return { 'Status' : 'No Content' }, 200

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in results]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        return { 'Status' : 'Success', 'Year' : year, 'Make' : make, 'Records_Found' : len(datajson), 'Data' : datajson }, 200

class YearModelList(Resource):
    def get(self, year, model):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM cars WHERE year=:year AND model LIKE :model;", {'year' : int(year), 'model' : '%'+(model.upper())+'%'})
        con.commit()
        
        results = cur.fetchall()
        if len(results) < 1:
            return { 'Status' : 'No Content' }, 200

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in results]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        return { 'Status' : 'Success', 'Year' : year, 'Model' : model, 'Records_Found' : len(datajson), 'Data' : datajson }, 200

class YearList(Resource):
    def get(self, year):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM cars WHERE year=?;", [year])
        con.commit()
        results = cur.fetchall()
        if len(results) < 1:
            return { 'Status' : 'No Content' }, 200

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in results]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        return { 'Status' : 'Success', 'Year': year, 'Records_Found' : len(datajson), 'Data' : datajson }, 200

class ComboList(Resource):
    def get(self, year, make, model):
        con = sqlite3.connect("./data.db")
        cur = con.cursor()
        if (model.lower() == 'any'):
            cur.execute("SELECT * FROM cars WHERE year=:year AND make LIKE :make AND model LIKE :model;", {'year' : int(year), 'make' : '%'+(make.upper())+'%', 'model' : '%'})
        else:
            cur.execute("SELECT * FROM cars WHERE year=:year AND make LIKE :make AND model LIKE :model;", {'year' : int(year), 'make' : '%'+(make.upper())+'%', 'model' : '%'+(model.upper())+'%'})
        
        results = cur.fetchall()
        if len(results) < 1:
            return { 'Status' : 'No Content' }, 200

        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in results]
        datatemp = json.dumps(data)
        datajson = json.loads(datatemp)

        return { 'Status' : 'Success', 'Year' : year, 'Make' : make, 'Model' : model, 'Records_Found' : len(datajson), 'Data' : datajson }, 200

api.add_resource(IdSearch, '/cars/id=<int:carid>')
api.add_resource(MakeList, '/cars/make=<string:make>')
api.add_resource(ModelList, '/cars/model=<string:model>')
api.add_resource(MakeModelList, '/cars/make=<string:make>&model=<string:model>')
api.add_resource(YearMakeList, '/cars/year=<int:year>&make=<string:make>')
api.add_resource(YearModelList, '/cars/year=<int:year>&model=<string:model>')
api.add_resource(YearList, '/cars/year=<int:year>')
api.add_resource(ComboList, '/cars/year=<int:year>&make=<string:make>&model=<string:model>')

if __name__ == '__main__':
    app.run(debug=True)