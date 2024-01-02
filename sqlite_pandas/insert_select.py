import sqlite3

con = sqlite3.connect("test.db")

# Create a cursor
cur = con.cursor()
# Drop table if already exists
cur.execute("DROP TABLE IF EXISTS transcript;")
# Create the table named transcript
cur.execute("CREATE TABLE transcript (name text, grade integer);")

# Demo Records
names = ['John', 'Mike', 'Jane', 'Bella']
grades = [90, 95, 92, 98]

# Insert the records
cur.executemany("INSERT into transcript values (?, ?)", zip(names, grades))


print(list(cur.execute("select * from transcript order by grade desc")))
# print(cur.fetchall())

#Select data using pandas
import pandas as pd
df = pd.read_sql("select * from transcript", con)
print(df)

# Commit all the transactions
con.commit()


