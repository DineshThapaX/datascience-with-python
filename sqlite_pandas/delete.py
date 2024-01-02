import sqlite3

con = sqlite3.connect("test.db")

# Create a cursor
cur = con.cursor()

#Display Existing Data in the Table
print(list(cur.execute("select * from transcript order by grade desc")))
# print(cur.fetchall())

# Delete Records
cur.execute("delete from transcript where name='John'")

#Display Records after delete in the Table
print(list(cur.execute("select * from transcript order by grade desc")))
# print(cur.fetchall())

# Commit all the transactions
con.commit()


