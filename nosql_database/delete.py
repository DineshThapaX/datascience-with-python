# Import the python libraries
from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
client = MongoClient("mongodb://localhost:27017")

# Connect to db
db=client.test
employee = db.employee

# Use the condition to choose the record
# and use the delete method
db.employee.delete_one({"Age":'32'})

Queryresult = employee.find_one({'Age':'32'})

pprint(Queryresult)