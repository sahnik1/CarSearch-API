# CarSearch API

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/sahnik1/CarSearch-API)

# LIVE AT:
### https://carsearch-api.herokuapp.com/

From my previous CarSearch Application, I decided to make the aggregated data I collected available for public use via a simple Web Api. The information available includes:

  - A Unique Car ID to Refer to a Specific Car in the Database
  - Year
  - Make
  - Model
  - Number of Recalls
  - Vehicles Affected by These Recalls
  - City Mileage (MPG)
  - Highway Mileage (MPG)
  - Combined Mileage (MPG)
  - Number of Cylinders (Engine)
  - Engine Displacement in Litres (eg 3.2L)
  - Transmission
  - Drive (eg 4WD)

# Installation
### Requirements:
* Python 3.7 or higher
* Flask and Flask-Restful
* SQLite 3

### Instructions:
* Ensure all Files are in the same Directory (including 'final.csv')
* From Terminal/Powershell run ```python store.py``` to make a ```data.db``` file for database
* From Terminal/Powershell run ```python run.py``` to make a dev server for running API
* Done!

# Sample JSON Output


## By Car ID:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/id=9002
```
#### Output:
```json
{
    "Status": "Success",
    "Data": [
        {
            "id": 9002,
            "year": 2018,
            "category": "STANDARD SPORT UTILITY VEHICLE 4WD",
            "make": "TOYOTA",
            "model": "HIGHLANDER HYBRID",
            "No_Of_Recalls": 8,
            "Vehicles_Affected": 200624,
            "City_MPG": 29,
            "Highway_MPG": 27,
            "Combined_MPG": 28,
            "Cylinders": 6,
            "Eng_Displ": 3.5,
            "Transmission": "AUTOMATIC (AV-S6)",
            "Drive": "ALL-WHEEL DRIVE"
        }   ]
}
```

## By Year Alone:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/year=2005
```
#### Output:
```json
{
    "Status": "Success",
    "Records_Found": 332,
    "Data": [
        {
            "id": 3365,
            "year": 2005,
            "category": "TWO SEATERS",
            "make": "ACURA",
            "model": "NSX",
            "No_Of_Recalls": 4,
            "Vehicles_Affected": 423910,
            "City_MPG": 16,
            "Highway_MPG": 22,
            "Combined_MPG": 18,
            "Cylinders": 6,
            "Eng_Displ": 3.0,
            "Transmission": "AUTOMATIC (S4)",
            "Drive": "REAR-WHEEL DRIVE"
        }, ... ]
}
```


## Given Year, Make & Model:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/year=2019,make=toyo,model=avalon
```
#### Output:
```json
{
    "Status": "Success",
    "Year": 2019,
    "Make": "toyo",
    "Model": "avalon",
    "Records_Found": 1,
    "Data": [
        {
            "id": 9062,
            "year": 2019,
            "category": "MIDSIZE CARS",
            "make": "TOYOTA",
            "model": "AVALON",
            "No_Of_Recalls": 77,
            "Vehicles_Affected": 13612407,
            "City_MPG": 22,
            "Highway_MPG": 31,
            "Combined_MPG": 25,
            "Cylinders": 6,
            "Eng_Displ": 3.5,
            "Transmission": "AUTOMATIC (S8)",
            "Drive": "FRONT-WHEEL DRIVE"
        }   ]
}
```
## Note
* The API is Flexible for Incomplete Makes or Models and therefore in the above example works for the make 'toyo'