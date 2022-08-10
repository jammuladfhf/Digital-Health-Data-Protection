# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:50:33 2022

@author: saido
"""

if 'next' not in st.session_state:
	st.session_state.next = 0

# Create a button which will increment the counter
next = st.button('Next')
if next:
    if st.session_state.next == 0:
        st.session_state.next == 1
        
def addData(cols, tag='Hospital Basic Details'):
    
    if tag == 'Hospital Basic Details':
        conn = sqlite3.connect('DHP.db', check_same_thread=False)
        cur=conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS hospitalform(hospitalname Text(100), address1 Text(100),  address2 Text(100), phonenumber Text(20), Hospitaltype Text(20), Hospitalownership Text(20));""")
        
        cur.execute("INSERT INTO hospitalform VALUES(?,?,?,?,?,?)", cols)
        conn.commit()
        conn.close()
        st.success("Hospital Data Successfully Submitted")