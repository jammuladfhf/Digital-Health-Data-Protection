# -*- coding: utf-8 -*-
"""
Created on Mon Aug  11 21:13:00 2022

@author: Narender Jammula
"""

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

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
HBD =[]
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
     
    if st.button('Submit'):
        cols = (Hospital_name, Address1, Address2, Phone_number, Hospital_type, Hospital_ownership)   
        HBD.append(cols)


# =============================================================================
# Tech = []
# if (selected == 'Technology'):
#     
#     st.title('Answer Technology Related Questions with Yes/No')
#     health_stored = st.selectbox("Are health data stored on computers ?", ('Yes', 'No'))
#     EHRs = st.selectbox("Meets criteria for meaningful use of EHRs ?", ('Yes', 'No'))
#     design_data_protection = st.selectbox("Is the design and configuration of the health system done with data protection in mind ?", ('Yes', 'No'))
#     design_config = st.selectbox("Is the by design and default incorporated from the onset of the technology selection, design and configuration ?", ('Yes', 'No'))
#     privacy_security = st.selectbox("Are privacy and security integrated into all healthcare apps, devices, and services from the start ?", ('Yes', 'No'))
#     encript_heatlth_data = st.selectbox("Have we incorporated encryption of health data with the design from the start ?", ('Yes', 'No'))
#     Question7 = st.selectbox("Question7", ('Yes', 'No'))
#     Question8 = st.selectbox("Question8", ('Yes', 'No'))
#     Question9 = st.selectbox("Question9", ('Yes', 'No'))
#     Question10 = st.selectbox("Question10", ('Yes', 'No'))
#     
#     if st.button('Submit'):
#         tech_cols = (health_stored, EHRs, design_data_protection, design_config, privacy_security,
#                      encript_heatlth_data, Question7,Question8,Question9,Question10)   
#         Tech.append(tech_cols)
# =============================================================================
    
    
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
  
    
if (selected == 'Predict'):

    st.title('Output')

        
    
