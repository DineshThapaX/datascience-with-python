import sqlite3

con = sqlite3.connect("test.db")

# Create a cursor
cur = con.cursor()

#Display Existing Data in the Table
print(list(cur.execute("select * from transcript order by grade desc")))
# print(cur.fetchall())

# Update Records
cur.execute("update transcript set grade = 50 where name = 'John'")

#Display Records after update in the Table
print(list(cur.execute("select * from transcript order by grade desc")))
# print(cur.fetchall())

# Commit all the transactions
con.commit()


