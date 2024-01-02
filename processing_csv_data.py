# import os
# print(os.getcwd())

# Reading a input.csv file
import pandas as pd
data = pd.read_csv('files/input.csv')
print (data)

# Reading Specific Rows
# Reading  First 5 rows for the column named salary
import pandas as pd
data = pd.read_csv('files/input.csv')

# Slice the result for first 5 rows
print(data[0:5]['salary'])

print("\n")
# Reading the the first five rows for 'name' and 'dept' columns
import pandas as pd
# Read the CSV file into a DataFrame
data = pd.read_csv("files/input.csv")
selected_data = data.loc[0:4, ['name', 'dept']]
# Print the selected data
print(selected_data)

print("\n")
# Reading Specific Columns
import pandas as pd
data = pd.read_csv('files/input.csv')

# Use the multi-axes indexing funtion
print (data.loc[:,['salary','name']])

print("\n")

# Reading Specific Columns and Rows
import pandas as pd
data = pd.read_csv('files/input.csv')

# Use the multi-axes indexing funtion
print(data.loc[[1,3,5], ['salary','name']])

print("\n")
# Reading Specific Columns for a Range of Rows
import pandas as pd
data = pd.read_csv('files/input.csv')

# Use the multi-axes indexing funtion
print(data.loc[2:6,['salary','name']])


