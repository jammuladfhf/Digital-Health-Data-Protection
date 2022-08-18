# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:56:42 2022

@author: saido
"""
# =============================================================================
# import uuid
# print (uuid.uuid1())
# import psycopg2
# import psycopg2.extras
# =============================================================================
from predict import predict_method



form_data = {"Hospital_name":"SOUTHEAST ALABAMA MEDICAL CENTER",
"Address1":"1108 ROSS CLARK CIRCLE",
"Address2":"HOUSTON",
"Phone_number":"3347938701",
"Hospital_type":"Acute Care Hospitals",
"Hospital_ownership":"Government - Hospital District or Authority",
"tech_health_stored":"Yes",
"tech_EHRs":"Yes",
"tech_design_data_protection":"Yes",
"tech_design_config":"Yes",
"tech_privacy_security":"Yes",
"tech_encript_heatlth_data":"Yes",
"tech_Question7":"Yes",
"tech_Question8":"Yes",
"tech_Question9":"Yes",
"tech_Question10":"Yes",
"cyber_health_stored":"Yes",
"cyber_EHRs":"Yes",
"cyber_design_data_protection":"Yes",
"cyber_design_config":"Yes",
"cyber_privacy_security":"Yes",
"cyber_encript_heatlth_data":"Yes",
"cyber_Question7":"Yes",
"cyber_Question8":"Yes",
"cyber_Question9":"Yes",
"cyber_Question10":"Yes"
}

# =============================================================================
# "cyber_health_stored":"Yes",
# "cyber_EHRs":"Yes",
# "cyber_design_data_protection":"Yes",
# "cyber_design_config":"Yes",
# "cyber_privacy_security":"Yes",
# "cyber_encript_heatlth_data":"Yes",
# "cyber_Question7":"Yes",
# "cyber_Question8":"Yes",
# "cyber_Question9":"Yes",
# "cyber_Question10":"Yes"
# =============================================================================

# =============================================================================
# individual_op, final_op = pp.main()
# =============================================================================
method1_predict =  predict_method(form_data, domain_count=2)
individual_op, final_op = method1_predict.method2()
print(individual_op, final_op )
# =============================================================================
# DB_HOST = "ec2-34-193-44-192.compute-1.amazonaws.com"
# DB_NAME = "d5n8kfftsqqq9e"
# DB_USER = "ksqexwhwzhjpni"
# DB_PASS = "493f23f9fe376b724970c8a2f50495307dff7f31bc9e3f40f6533a237721e691"
# 
# conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# 
# 
# # =============================================================================
# # cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")
# # =============================================================================
# # =============================================================================
# # cur.execute("INSERT INTO  student values (?, ?)",(1234, 'jammula'))
# # =============================================================================
# 
# cur.execute('select * from student;')
# print(cur.fetchall())
# 
# conn.commit()
# 
# cur.close()
# =============================================================================

# =============================================================================
# conn.close()
# =============================================================================


