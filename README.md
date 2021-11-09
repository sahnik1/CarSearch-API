# CarSearch API

# LIVE AT:
### https://carsearch-api.herokuapp.com/cars

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
    "Year": 2005,
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

## By Make Alone:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/make=Tesla
```
#### Output:
```json
{
    "Status": "Success",
    "Make": "Tesla",
    "Records_Found": 12,
    "Data": [
        {
            "id": 6844,
            "year": 2012,
            "category": "LARGE CARS",
            "make": "TESLA",
            "model": "MODEL S",
            "No_Of_Recalls": 21,
            "Vehicles_Affected": 56754,
            "City_MPG": 88,
            "Highway_MPG": 90,
            "Combined_MPG": 89,
            "Cylinders": 0,
            "Eng_Displ": 0.0,
            "Transmission": "AUTOMATIC (A1)",
            "Drive": "REAR-WHEEL DRIVE"
        }, ... ]
}
```

## By Model Alone:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/model=model%20s
```
#### Output:
```json
{
    "Status": "Success",
    "Model": "model s",
    "Records_Found": 8,
    "Data": [
        {
            "id": 6844,
            "year": 2012,
            "category": "LARGE CARS",
            "make": "TESLA",
            "model": "MODEL S",
            "No_Of_Recalls": 21,
            "Vehicles_Affected": 56754,
            "City_MPG": 88,
            "Highway_MPG": 90,
            "Combined_MPG": 89,
            "Cylinders": 0,
            "Eng_Displ": 0.0,
            "Transmission": "AUTOMATIC (A1)",
            "Drive": "REAR-WHEEL DRIVE"
        }, ... ]
}
```

## Given Make & Model:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/make=toyo&model=avalon
```
#### Output:
```json
{
    "Status": "Success",
    "Make": "toyo",
    "Model": "avalon",
    "Records_Found": 25,
    "Data": [
        {
            "id": 689,
            "year": 1995,
            "category": "LARGE CARS",
            "make": "TOYOTA",
            "model": "AVALON",
            "No_Of_Recalls": 77,
            "Vehicles_Affected": 13612407,
            "City_MPG": 18,
            "Highway_MPG": 26,
            "Combined_MPG": 21,
            "Cylinders": 6,
            "Eng_Displ": 3.0,
            "Transmission": "AUTOMATIC 4-SPD",
            "Drive": "FRONT-WHEEL DRIVE"
        }, ... ]
}
```

## Given Year & Model:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/year=2019&model=model%20x
```
#### Output:
```json
{
    "Status": "Success",
    "Year": 2019,
    "Model": "model x",
    "Records_Found": 1,
    "Data": [
        {
            "id": 11098,
            "year": 2019,
            "category": "STANDARD SPORT UTILITY VEHICLE 4WD",
            "make": "TESLA",
            "model": "MODEL X",
            "No_Of_Recalls": 4,
            "Vehicles_Affected": 4890,
            "City_MPG": 91,
            "Highway_MPG": 95,
            "Combined_MPG": 93,
            "Cylinders": 0,
            "Eng_Displ": 0.0,
            "Transmission": "AUTOMATIC (A1)",
            "Drive": "ALL-WHEEL DRIVE"
        }   ]
}
```

## Given Year & Make:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/year=2019&make=toyo
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

## Given Year, Make & Model:

#### Query: 
```html
https://carsearch-api.herokuapp.com/cars/year=2019&make=toyo&model=avalon
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

### Note
* The API is Flexible for Incomplete Makes or Models and therefore in the above example works for the make 'toyo'