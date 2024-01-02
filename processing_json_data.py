# Read the json file
import pandas as pd
data = pd.read_json("files/input.json")
print(data)

print("\n")
# Reading Specific Columns and Rows
import pandas as pd
data = pd.read_json("files/input.json")
print(data.loc[[1,3,5], ['Name','Salary']])

print("\n")
# Reading JSON file as Records
import pandas as pd
data = pd.read_json('files/input.json')
print(data.to_json(orient='records', lines=True))

