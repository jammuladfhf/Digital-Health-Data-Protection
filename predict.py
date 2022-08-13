# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:36:39 2022

@author: Narender Jammula
"""
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# =============================================================================
# form_data = {"Hospital_name":"SOUTHEAST ALABAMA MEDICAL CENTER",
# "Address1":"1108 ROSS CLARK CIRCLE",
# "Address2":"HOUSTON",
# "Phone_number":"3347938701",
# "Hospital_type":"Acute Care Hospitals",
# "Hospital_ownership":"Government - Hospital District or Authority",
# "tech_health_stored":"Yes",
# "tech_EHRs":"Yes",
# "tech_design_data_protection":"Yes",
# "tech_design_config":"Yes",
# "tech_privacy_security":"Yes",
# "tech_encript_heatlth_data":"Yes",
# "tech_Question7":"Yes",
# "tech_Question8":"Yes",
# "tech_Question9":"Yes",
# "tech_Question10":"Yes",
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
# }
# =============================================================================
class predict_method:
    
    def __init__(self, form_data, domain_count):
        self.form_data = form_data
        self.domain_count = domain_count
         
    # replace yes and no with 1 and 0
    def replace_yes_no(self):
        replaced_df = self.form_data
        for k, v in replaced_df.items():
            if v =='Yes':
                replaced_df[k] = 1
            elif v =='No':
                replaced_df[k] = 0
            else:
                replaced_df[k] = v
        return replaced_df
    
    #risk level based on risk value
    def risk_level(self, num):
        if 0 <= num <= 4:
            return 'High Risk'
        elif 5 <= num <= 7:
            return 'Medium Risk'
        elif 8 <= num <= 10:
            return 'Low Risk'
     
    #predict the final output    
    def final_op(self, all_risk_values, domain_count):
        
        low_count = 0
        for val in all_risk_values:
            if val == 'Low Risk':
                low_count +=1
                
        if low_count < domain_count:
            return 'Non-Compliant'
        else:
            return 'Compliant'
     
    # domain level output    
    def domain_op(self, df, regex_tag):
        
        domain_df = df.filter(regex=regex_tag)
        domain_df.loc[:,'sum'] = domain_df.sum(axis=1)
        domain_df.loc[:,'count'] = domain_df.shape[1] - 1
        domain_df.loc[:,'risk_scale'] = domain_df['sum']/domain_df['count']*10
        domain_df.loc[:,'risk_level'] = domain_df['risk_scale'].apply(self.risk_level)
        tech_risk = domain_df.risk_level.values[0]
        return tech_risk
        
    
    def main(self):
        
        form_data_replace = self.replace_yes_no()
        df = pd.DataFrame([form_data_replace], columns = form_data_replace.keys())
        
        tech_op = self.domain_op(df, regex_tag='tech')
        cyber_op = self.domain_op(df, regex_tag='cyber')
        all_risk_values = {'technology':tech_op, 'cyber_security':cyber_op}
        
        return all_risk_values, self.final_op(all_risk_values.values(), self.domain_count)

# =============================================================================
# 
# if __name__ == '__main__':     
#    final_op = predict_method.main()
#    print('Final Output')
# =============================================================================



















# =============================================================================
# class predict_method():
# =============================================================================

# =============================================================================
# def __init__(self):
#     return 
# 
# =============================================================================

# =============================================================================
# 
# def method1(self, ):
#     ''' 
#     This method does not involve any Machine Learning
#     Algorithms, it a rule based approach
#     '''
#     
#     
#     
#     
#     
#     
#     return
# # =============================================================================
# # def method2():
# #    
# #     return
# # =============================================================================
# 
# =============================================================================
