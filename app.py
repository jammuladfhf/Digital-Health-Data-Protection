# -*- coding: utf-8 -*-
"""
Created on Mon Aug  11 21:13:00 2022

@author: Narender Jammula
"""

#'This version is without NEXT button'

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
					   hospital_type      TEXT, hospital_ownership TEXT, \
                       tech_health_stored  TEXT, \
					   tech_EHRs TEXT,  tech_design_data_protection TEXT, tech_design_config TEXT, \
					   tech_privacy_security TEXT, tech_encript_heatlth_data TEXT, tech_Question7 TEXT, \
					   tech_Question8 TEXT, tech_Question9  TEXT, tech_Question10 TEXT,  \
                       cyber_data_breach TEXT, \
                       cyber_prepared_for_health_breach TEXT, cyber_internal_threat TEXT, cyber_external_threat TEXT, \
                       cyber_data_breach_procedure TEXT, cyber_process_for_policy_containment TEXT, cyber_liability_DHD TEXT, \
                       cyber_threat_againt_DHD TEXT, cyber_security_measures TEXT, cyber_Question10 TEXT,  \
                       Predict TEXT  \
					);")
        
    cur.execute("""INSERT INTO hospital_data (hospital_name, address1, address2, phone_number, hospital_type, \
                hospital_ownership, tech_health_stored, tech_EHRs, tech_design_data_protection, tech_design_config, \
                tech_privacy_security, tech_encript_heatlth_data, tech_Question7, tech_Question8, tech_Question9, \
                tech_Question10, cyber_data_breach, cyber_prepared_for_health_breach, cyber_internal_threat,   \
                cyber_external_threat, cyber_data_breach_procedure, cyber_process_for_policy_containment, \
                cyber_liability_DHD, cyber_threat_againt_DHD, cyber_security_measures, 
                cyber_Question10, Predict) VALUES{}; """.format(values))
        
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
                             'Predict'],
                            icons = ['activity', 'app', 'shield-lock','bookmark-fill','diagram-2','card-checklist'],
                            default_index=0)

    
if (selected == 'Hospital Basic Details'):
    
    st.session_state = {}
    st.title('Enter Hospital Details')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Hospital_name = st.text_input('Hospital Name*')
    with col2:
        Address2 = st.text_input('Address 2')  
    with col3:
        Hospital_type = st.text_input('Hospital Type')
        
    with col1:
        Address1 = st.text_input('Address 1')
    with col2:
        Phone_number = st.text_input('Phone Number')
    with col3:
        Hospital_ownership = st.text_input('Hospital Ownership')
        
        
    if  st.button('Save'):
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
        

#Technology

if (selected == 'Technology'):
     
    st.title('Technology Domain')
    
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
         
#Cybersecurity           
if (selected == 'Cybersecurity'):  
    
    st.title('Cybersecurity Domain')
    
    data_breach = st.selectbox("Recording where necessary, reporting health data breaches ?", ('Select','Yes', 'No'))
    prepared_for_health_breach = st.selectbox("Are you prepared for any health data breach ?", ('Select','Yes', 'No'))
    internal_threat = st.selectbox("Are there internal threat to digital health data ?", ('Select','Yes', 'No'))
    external_threat = st.selectbox("Are there external threat to Digital health data ?", ('Select','Yes', 'No'))
    data_breach_procedure = st.selectbox("Do you have any data breach incidence reporting procedures ?", ('Select','Yes', 'No'))
    process_for_policy_containment = st.selectbox("Do you have a process or policy for containment ?", ('Select','Yes', 'No'))
    liability_DHD = st.selectbox("What liability does digital health data and corresponding sharing, linking and reuse practices pose to data protection ?", ('Select','Yes', 'No'))
    threat_againt_DHD = st.selectbox("Is there any liability with the threat against digital health data ?", ('Select','Yes', 'No'))
    security_measures = st.selectbox("Implemented appropriate security measures ?", ('Select','Yes', 'No'))
    Question10 = st.selectbox("Question10", ('Select','Yes', 'No'))
 
    if st.button('Save'):
        if (data_breach == 'Select') or (prepared_for_health_breach == 'Select') or (internal_threat == 'Select') or (external_threat == 'Select') or \
           (data_breach_procedure == 'Select') or (process_for_policy_containment == 'Select') or (liability_DHD == 'Select') or \
           (threat_againt_DHD == 'Select') or (security_measures == 'Select')or (Question10 == 'Select'):
               st.warning('Please fill all the required fields with yes or no'.upper())  
        else:  
            st.session_state['cyber_data_breach'] = data_breach
            st.session_state['cyber_prepared_for_health_breach'] = prepared_for_health_breach
            st.session_state['cyber_internal_threat'] = internal_threat
            st.session_state['cyber_external_threat'] = external_threat
            st.session_state['cyber_data_breach_procedure'] = data_breach_procedure
            st.session_state['cyber_process_for_policy_containment'] = process_for_policy_containment
            st.session_state['cyber_liability_DHD'] = liability_DHD
            st.session_state['cyber_threat_againt_DHD'] = threat_againt_DHD
            st.session_state['cyber_security_measures'] = security_measures
            st.session_state['cyber_Question10'] = Question10
            st.success("Saved Successfully")

    
 
if (selected == 'Predict'):
    st.title('Output')
    predict_method =  predict_method(st.session_state, domain_count=2)
    individual_op, final_op = predict_method.method2()
    
    st.session_state['predict'] = final_op
    hospital_name = st.session_state['Hospital_name']
    st.header(f'{hospital_name} is {final_op}')
    risk_table = pd.DataFrame()
    risk_table['Domain Name'] = individual_op.keys()
    risk_table['Domain Name'] = risk_table['Domain Name'].apply(lambda x:x.upper())
    risk_table['Risk level'] = individual_op.values()
    risk_table.style.apply(lambda x: ["background: red"
                            if v == 'Medium Risk' else "" for v in x])
    st.dataframe(risk_table)

    try:
        table_creation(tuple(st.session_state.values()))
        st.success("Successfully Saved")
    except Exception as e:
        st.warning(e)
        st.warning('Please fill all the Required Pages'.upper())

    
