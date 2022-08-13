# -*- coding: utf-8 -*-
"""
Created on Mon Aug  11 21:13:00 2022

@author: Narender Jammula
"""
################################# Import Libraries ############################
#streamlit libraries
from predict import predict_method
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

#postgres - Database libraries
import psycopg2
import psycopg2.extras

#custom modules
from predict import predict_method


####################### Main Code  ############################################
#Credentials
DB_HOST = "ec2-34-193-44-192.compute-1.amazonaws.com"
DB_NAME = "d5n8kfftsqqq9e"
DB_USER = "ksqexwhwzhjpni"
DB_PASS = "493f23f9fe376b724970c8a2f50495307dff7f31bc9e3f40f6533a237721e691"

#UDF
def table_creation(values):  
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    #while testing uncomment drop query and for final data comment it
    cur.execute("Drop table hospital_data;") 
    cur.execute("CREATE TABLE IF NOT EXISTS hospital_data(hospital_name TEXT PRIMARY KEY  NOT NULL, \
					   address1           TEXT, address2           TEXT, phone_number       TEXT, \
					   hospital_type      TEXT, hospital_ownership TEXT, health_stored  TEXT, \
					   EHRs TEXT,  design_data_protection TEXT, design_config TEXT, \
					   privacy_security TEXT, encript_heatlth_data TEXT, Question7 TEXT, \
					   Question8 TEXT, Question9  TEXT, Question10 TEXT, Predict TEXT \
					);")
    cur.execute("""INSERT INTO hospital_data (hospital_name, address1, address2, phone_number, hospital_type, \
                hospital_ownership, health_stored, EHRs, design_data_protection, design_config, \
                privacy_security, encript_heatlth_data, Question7, Question8, Question9, \
                Question10, Predict) VALUES{}; """.format(values))
    conn.commit() 
    cur.close() 
    conn.close()

with st.sidebar:
    selected = option_menu('Digital Health Data Protection', 
                            ['Hospital Basic Details', 
                             'Technology',
                             'Cybersecurity',
                             'Legislation',
                             'Digital Data Governance',   
                             'Predict',
                             'DataBase'],
                            icons = ['activity', 'app', 'shield-lock','bookmark-fill','diagram-2','card-checklist'],
                            default_index=0)

if (selected == 'Hospital Basic Details'):
    st.session_state = {}
    st.title('Enter Hospital Details')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Hospital_name = st.text_input('Hospital Name*')
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
        if Hospital_name != '':
            st.session_state['Hospital_name'] = Hospital_name
            st.session_state['Address1'] = Address1
            st.session_state['Address2'] = Address2
            st.session_state['Phone_number'] = Phone_number
            st.session_state['Hospital_type'] = Hospital_type
            st.session_state['Hospital_ownership'] = Hospital_ownership
            st.success("Saved Successfully")
        else:
            st.warning('Fill Mandatory Fields')


if (selected == 'Technology'):
    
    st.title('Answer Technology Related Questions with Yes/No')
    
    health_stored = st.selectbox("Are health data stored on computers ?", ('Select','Yes', 'No'))
    EHRs = st.selectbox("Meets criteria for meaningful use of EHRs ?", ('Select','Yes', 'No'))
    design_data_protection = st.selectbox("Is the design and configuration of the health system done with data protection in mind ?", ('Select','Yes', 'No'))
    design_config = st.selectbox("Is the by design and default incorporated from the onset of the technology selection, design and configuration ?", ('Select','Yes', 'No'))
    privacy_security = st.selectbox("Are privacy and security integrated into all healthcare apps, devices, and services from the start ?", ('Select','Yes', 'No'))
    encript_heatlth_data = st.selectbox("Have we incorporated encryption of health data with the design from the start ?", ('Select','Yes', 'No'))
    Question7 = st.selectbox("Question7", ('Select','Yes', 'No'))
    Question8 = st.selectbox("Question8", ('Select','Yes', 'No'))
    Question9 = st.selectbox("Question9", ('Select','Yes', 'No'))
    Question10 = st.selectbox("Question10", ('Select', 'Yes', 'No'))
    
    if st.button('Save'):
        if (health_stored == 'Select') or (EHRs == 'Select') or (design_data_protection == 'Select') or (design_config == 'Select') or \
           (privacy_security == 'Select') or (encript_heatlth_data == 'Select') or (Question7 == 'Select') or (Question8 == 'Select') or \
           (Question9 == 'Select') or (Question10 == 'Select'):
               st.warning('Please fill all the required fields with yes or no'.upper())  
        else:  
            st.session_state['tech_health_stored'] = health_stored
            st.session_state['tech_EHRs'] = EHRs
            st.session_state['tech_design_data_protection'] = design_data_protection
            st.session_state['tech_design_config'] = design_config
            st.session_state['tech_privacy_security'] = privacy_security
            st.session_state['tech_encript_heatlth_data'] = encript_heatlth_data
            st.session_state['tech_Question7'] = Question7
            st.session_state['tech_Question8'] = Question8
            st.session_state['tech_Question9'] = Question9
            st.session_state['tech_Question10'] = Question10
            st.success("Saved Successfully")
         
# =============================================================================
# if (selected == 'Cybersecurity'):  
#     
#     st.title('Answer Cybersecurity Related Questions with Yes/No')
#     
#     data_breach = st.text_input("Recording where necessary, reporting health data breaches ?")
#     prepared_for_health_breach = st.text_input("Are you prepared for any health data breach ?")
#     internal_threat = st.text_input("Are there internal threat to digital health data ?")
#     external_threat = st.text_input("Are there external threat to Digital health data ?")
#     data_breach_procedure = st.text_input("Do you have any data breach incidence reporting procedures ?")
#     process_for_policy_containment = st.text_input("Do you have a process or policy for containment ?")
#     liability_DHD = st.text_input("What liability does digital health data and corresponding sharing, linking and reuse practices pose to data protection ?")
#     threat_againt_DHD = st.text_input("Is there any liability with the threat against digital health data ?")
#     security_measures = st.text_input("Implemented appropriate security measures ?")
#     Question10 = st.text_input("Question10")
#   
if (selected == 'Predict'):
    st.title('Output')
    method1_predict =  predict_method(st.session_state, domain_count=1)
    individual_op, final_op = method1_predict.main()
    st.session_state['predict'] = final_op
    st.write(st.session_state)

    try:
        table_creation(tuple(st.session_state.values()))
        st.success("Successfully Saved")
    except Exception as e:
        st.warning(e)
        st.warning('Please fill all the Required Pages'.upper())

    
