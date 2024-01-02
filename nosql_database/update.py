#Upating Record
# Import the python libraries
from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
client = MongoClient("mongodb://localhost:27017")

# Connect to db
db=client.test
employee = db.employee

# Use the condition to choose the record
# and use the update method
db.employee.update_one(
        {"Age":'42'},
        {
        "$set": {
            "Name":"Ram",
            "Age":'32',
            "Address":"London, UK"
        }
        }
    )

Queryresult = employee.find_one({'Age':'32'})

pprint(Queryresult)