# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:48:15 2022

@author: saido
"""
import pandas as pd
import streamlit as st
import sqlite3
conn = sqlite3.connect('demo.db')
cur = conn.cursor()

import uuid
DIGITS = 8  # number of hex digits of the UUID to use
print(uuid.uuid4().hex[:DIGITS] )  #{cid: int(uuid.uuid4().hex[:DIGITS], base=16) for cid in original_ids}






# =============================================================================
# def form():
#     st.write("This is a form")
#     with st.form(key='Information form'):
#         name=st.text_input("Enter your name: ")
#         age=st.text_input("Enter age:")
#         submission = st.form_submit_button(label='Submit')
#         if submission == True:
#             addData(name, age)
#         printdata()
#             
# def addData(name,age):
#     cur.execute(""" Create table if not exists clg_form(Name Text(50), Age Text(50));""")
#     cur.execute("insert into clg_form values (?, ?)",(name, age))
#     conn.commit()
#     conn.close()
#     st.success('Successfully Submited')
# 
# def printdata():
#     conn1 = sqlite3.connect('demo.db')
#     cur1 = conn1.cursor()
#     df = pd.read_sql(" select * from clg_form ", con=conn1)
#     st.write(df)
#     
#     
# form()
# =============================================================================
