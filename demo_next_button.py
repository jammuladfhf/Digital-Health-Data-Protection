# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:43:34 2022

@author: saido
"""
import pickle as pkle
new_choice = ['Hospital Basic Details', 'Technology','Cybersecurity', 'Legislation', 'Digital Data Governance', 'Predict', 'DataBase']

selected = 'Technology'
pkle.dump(new_choice.index(selected), open('next.p', 'wb'))   
next_clicked = pkle.load(open('next.p', 'rb'))
print(next_clicked)
# =============================================================================
# import streamlit as st
# 
# import os.path
# 
# # create a button in the side bar that will move to the next page/radio button choice
# next = st.sidebar.button('Next on list')
# 
# # will use this list and next button to increment page, MUST BE in the SAME order
# # as the list passed to the radio button
# new_choice = ['Home','Resources','Gallery','Vision','About']
# 
# # This is what makes this work, check directory for a pickled file that contains
# # the index of the page you want displayed, if it exists, then you pick up where the
# #previous run through of your Streamlit Script left off,
# # if it's the first go it's just set to 0
# if os.path.isfile('next.p'):
#     next_clicked = pkle.load(open('next.p', 'rb'))
#     # check if you are at the end of the list of pages
#     if next_clicked == len(new_choice):
#         next_clicked = 0 # go back to the beginning i.e. homepage
# else:
#     next_clicked = 0 #the start
# 
# # this is the second tricky bit, check to see if the person has clicked the
# # next button and increment our index tracker (next_clicked)
# if next:
#     #increment value to get to the next page
#     next_clicked = next_clicked +1
# 
#     # check if you are at the end of the list of pages again
#     if next_clicked == len(new_choice):
#         next_clicked = 0 # go back to the beginning i.e. homepage
# 
# # create your radio button with the index that we loaded
# choice = st.sidebar.radio("go to",('Home','Resources', 'Gallery', 'Vision', 'About'), index=next_clicked)
# 
# # pickle the index associated with the value, to keep track if the radio button has been used
# pkle.dump(new_choice.index(choice), open('next.p', 'wb'))
# 
# # finally get to whats on each page
# if choice == 'Home':
#     st.write('this is home')
# elif choice == 'Resources':
#     st.write('here is a resources page')
# elif choice == 'Gallery':
#     st.write('A Gallery of some sort')
# elif choice == 'Vision':
#     st.write('The Vision')
# elif choice == 'About':
#     st.write('About page')
# =============================================================================
