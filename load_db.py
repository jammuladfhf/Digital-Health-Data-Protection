# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:28:15 2022

@author: Narender Jammula
"""
import sqlite3
conn = sqlite3.connect('DHDP.db')
#conn = sqlite3.connect('DHDP.db', check_same_thread=False)
cursorObj = conn.cursor()
cursorObj.execute("SELECT * FROM hospitalform1")
rows = cursorObj.fetchall()

for row in rows:
   print(row)
   
cursorObj.close()  


def sql_connection():
   try:
     conn = sqlite3.connect('DHDP.db')
     return conn
   except Error:
     print(Error)
 
def sql_table(conn, cols):
   cursorObj = conn.cursor()
# Create the table
   cursorObj.execute("CREATE TABLE IF NOT EXISTS hospitalform(hospital_name Text(100), address1 Text(100),  address2 Text(100), phone_number Text(20), Hospital_type Text(20), Hospital_ownership Text(20));")
# Insert records
   cursorObj.execute("INSERT INTO hospitalform VALUES(?,?,?,?,?,?);", cols)
   conn.commit()
   cursorObj.execute("SELECT * FROM hospitalform")
   rows = cursorObj.fetchall()
   print("Agent details:")
   for row in rows:
       print(row)