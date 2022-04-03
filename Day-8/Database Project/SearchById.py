#Search the records based on Customer id from database

import sqlite3

con=sqlite3.connect('hrsystem.db')

cur=con.cursor()

isFound=False
cid=int(input('Enter customer id:'))

for record in cur.execute('SELECT * FROM Customer where cid='+str(cid)):
    isFound=True
    print("CID=",record[0],"CName=",record[1],"CAge=",record[2])
    break

if(isFound==False):
    print("Record does not exists")

con.close()

input()
