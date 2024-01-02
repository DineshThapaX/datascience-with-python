# Reading an Excel File
import pandas as pd
data = pd.read_excel('files/input.xlsx')
print (data)

print("\n")
# Reading Specific Columns and Rows
import pandas as pd
data = pd.read_excel('files/input.xlsx')
print(data.loc[[1,2,3,5],['name','dept']])

print("\n")
# Reading Multiple Excel Sheets
import pandas as pd
with pd.ExcelFile('files/input.xlsx') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')

print("****Result Sheet 1****")
print (df1[0:5]['salary'])

print("")

print("***Result Sheet 2****")
print (df2[0:5]['zipcode'])

print("\n")
#Question: Read Student Name, Salary and Department of 2,4 and 5 students from Sheet 1 and
# name and Zip code of 6,7, and 8 students from sheet 2
import pandas as pd
with pd.ExcelFile('files/input.xlsx') as xls:
    data1 = pd.read_excel(xls, 'Sheet1')
    data2 = pd.read_excel(xls, 'Sheet2')

print("Sheet 1 Data:")
print(data1.loc[[1,2,3],['name','salary','dept']])
print("\n")
print("Sheet 2 Data:")
print(data2.loc[[5,6,7],['name','zipcode']])