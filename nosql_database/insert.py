# Inserting Data
# Import the python libraries
from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
# In my case, my client is mongodb://localhost:27017
client = MongoClient("mongodb://localhost:27017")

# Connect to the test db
db=client.test

# Use the employee collection
employee = db.employee
employee_details = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}

# Use the insert method
result = employee.insert_one(employee_details)

# Query for the inserted document.
Queryresult = employee.find_one({'Age': '42'})
pprint(Queryresult)

