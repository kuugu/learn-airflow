import sqlite3

con = sqlite3.connect('/home/kuugu/airflow/airflow.db')

print (con)

# creating a database cursor 
cur = con.cursor() 

# list all tables 
cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
print (cur.fetchall()) 

# print records from table "ab_user"
cur.execute('SELECT * FROM ab_user LIMIT 10')
print (cur.fetchall())
