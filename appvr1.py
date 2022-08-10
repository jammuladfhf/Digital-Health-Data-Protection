# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:13:00 2022

@author: Narender Jammula
"""

import streamlit as st
#import pickle
import pandas as pd
from streamlit_option_menu import option_menu
import sqlite3
from sqlite3 import Error
    
def add_data(cols):
    conn = sqlite3.connect('DHDP.db', check_same_thread=False)
    cursorObj = conn.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS hospitalform1(hospital_name Text(100), address1 Text(100),  address2 Text(100), phone_number Text(20), Hospital_type Text(20), Hospital_ownership Text(20));")
    cursorObj.execute("INSERT INTO hospitalform1 VALUES(?, ?, ?, ?, ?, ?);", cols)
    conn.commit()
    conn.close()
    st.success('Successfully Submited')

with st.sidebar:
    selected = option_menu('Digital Health Data Protection', 
                            ['Hospital Basic Details', 
                             'Technology',
                             'Cybersecurity',
                             'Legislation',
                             'Digital Data Governance',   
                             'Submit',
                             'DataBase'],
                            icons = ['activity', 'app', 'shield-lock','bookmark-fill','diagram-2','card-checklist'],
                            default_index=0)
hbd =[]
if (selected == 'Hospital Basic Details'):
    
    st.title('Enter Hospital Details')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Hospital_name = st.text_input('Hospital Name')
    with col2:
        Address1 = st.text_input('Address 1')
    with col3:
        Address2 = st.text_input('Address 2')
    with col1:
        Phone_number = st.text_input('Phone Number')
    with col2:
        Hospital_type = st.text_input('Hospital Type')
    with col3:
        Hospital_ownership = st.text_input('Hospital Ownership')
     
    if st.button('Save'):
        cols = (Hospital_name, Address1, Address2, Phone_number, Hospital_type, Hospital_ownership)   
        hbd.append(cols)
        add_data(cols)


if (selected == 'Technology'):
    
    st.title('Answer Technology Related Questions with Yes/No')
    
    health_stored = st.text_input("Are health data stored on computers ?")
    EHRs = st.text_input("Meets criteria for meaningful use of EHRs ?")
    design_data_protection = st.text_input("Is the design and configuration of the health system done with data protection in mind ?")
    design_config = st.text_input("Is the by design and default incorporated from the onset of the technology selection, design and configuration ?")
    privacy_security = st.text_input("Are privacy and security integrated into all healthcare apps, devices, and services from the start ?")
    encript_heatlth_data = st.text_input("Have we incorporated encryption of health data with the design from the start ?")
    Question7 = st.text_input("Question7")
    Question8 = st.text_input("Question8")
    Question9 = st.text_input("Question9")
    Question10 = st.text_input("Question10")
    
    
if (selected == 'Cybersecurity'):
    
    st.title('Answer Cybersecurity Related Questions with Yes/No')
    
    data_breach = st.text_input("Recording where necessary, reporting health data breaches ?")
    prepared_for_health_breach = st.text_input("Are you prepared for any health data breach ?")
    internal_threat = st.text_input("Are there internal threat to digital health data ?")
    external_threat = st.text_input("Are there external threat to Digital health data ?")
    data_breach_procedure = st.text_input("Do you have any data breach incidence reporting procedures ?")
    process_for_policy_containment = st.text_input("Do you have a process or policy for containment ?")
    liability_DHD = st.text_input("What liability does digital health data and corresponding sharing, linking and reuse practices pose to data protection ?")
    threat_againt_DHD = st.text_input("Is there any liability with the threat against digital health data ?")
    security_measures = st.text_input("Implemented appropriate security measures ?")
    Question10 = st.text_input("Question10")
  
    
if (selected == 'Submit'):

    st.title('Output')

if (selected == 'DataBase'):
    st.title('Final DataBase')
    conn_op = sqlite3.connect('DHDP.db')
    cursor_op = conn_op.cursor()
    df = pd.read_sql("Select * from hospitalform1", con=conn_op)
    st.write(df)
    



        
    
