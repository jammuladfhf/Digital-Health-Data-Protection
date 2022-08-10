# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:28:15 2022

@author: Narender Jammula
"""
import sqlite3
import pandas as pd

try:
  conn = sqlite3.connect('demo.db')
  conn.close()
  print(conn)
except Error:
  print(Error)
# =============================================================================
# conn = sqlite3.connect('C:\\Users\\saido\\OneDrive\\Desktop\\Upwork\\Digitalhealth data protection\\Streamlit for DHProj\\Digital-Health-Data-Protection\\demo.db')
# =============================================================================
cursorObj = conn.cursor()
# =============================================================================
# cursorObj.execute("insert into clg_form values (?, ?)",('ajja', 'age'))
# =============================================================================
cursorObj.execute("select * from clg_form")
display(df)
# =============================================================================
# import sqlite3
# def sql_table(cols):
#    print('table entered')
#    conn = sqlite3.connect('DHDP.db', check_same_thread=False)
#    cursorObj = conn.cursor()
#    # Create the table
# # =============================================================================
# #    cursorObj.execute("DROP TABLE hospitalform1;")
# # =============================================================================
# # =============================================================================
# #    cursorObj.execute("CREATE TABLE IF NOT EXISTS hospitalform1(hospital_name Text(100), address1 Text(100),  address2 Text(100), phone_number Text(20), Hospital_type Text(20), Hospital_ownership Text(20));")
# #    # Insert records
# #    cursorObj.execute("INSERT INTO hospitalform1 VALUES(?, ?, ?, ?, ?, ?);", cols)
# #    conn.commit()
# # =============================================================================
#    cursorObj.execute("SELECT * FROM hospitalform1")
#    rows = cursorObj.fetchall()
#    for row in rows:
#        print(row) 
#    if (conn):
#        conn.close()
# 
# cols = ('matric', '1-8-15/1/A, aravinda ndra Nagar Colony', '1-8-15/1/A, Ravindra Nagar Colony', '8801214001', 'ahsbs', 'skjakjs')
# sql_table(cols)  
# =============================================================================
# =============================================================================
# import sqlite3
# conn = sqlite3.connect('DHDP.db')
# #conn = sqlite3.connect('DHDP.db', check_same_thread=False)
# cursorObj = conn.cursor()
# cursorObj.execute("SELECT * FROM hospitalform1")
# rows = cursorObj.fetchall()
# for row in rows:
#     print(row)
# =============================================================================
# =============================================================================

#    
# cursorObj.close()  
# 
# 
# def sql_connection():
#    try:
#      conn = sqlite3.connect('DHDP.db')
#      return conn
#    except Error:
#      print(Error)
#  
# def sql_table(conn, cols):
#    cursorObj = conn.cursor()
# # Create the table
#    cursorObj.execute("CREATE TABLE IF NOT EXISTS hospitalform(hospital_name Text(100), address1 Text(100),  address2 Text(100), phone_number Text(20), Hospital_type Text(20), Hospital_ownership Text(20));")
# # Insert records
#    cursorObj.execute("INSERT INTO hospitalform VALUES(?,?,?,?,?,?);", cols)
#    conn.commit()
#    cursorObj.execute("SELECT * FROM hospitalform")
#    rows = cursorObj.fetchall()
#    print("Agent details:")
#    for row in rows:
#        print(row)
# =============================================================================
