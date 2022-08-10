# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:05:10 2022

@author: saido
"""

import sqlite3
 
from sqlite3 import Error
 
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
       
cols = ('Matrix', 'bangalore', 'srinagar', '829917991', 'a', 'gov')      
sqllite_conn = sql_connection()
sql_table(sqllite_conn, cols)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")