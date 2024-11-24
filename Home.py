import json 
import requests 
from streamlit_extras.app_logo import add_logo
import streamlit as st 
from streamlit_lottie import st_lottie 
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

# Create API.xlsx if not present
import sys, os
workingDirectory = os.getcwd()
costDirectory = os.path.join(workingDirectory, "cost_breakdown")
file_path = os.path.join(costDirectory, 'API Cost.xlsx')
if not os.path.exists(file_path):
    columns = ['Date', 'Processing Stage', 'Query', 'Total Input Tokens', 'Total Output Tokens', 'Total Cost']
    df = pd.DataFrame(columns=columns)
    df.to_excel('cost_breakdown/API Cost.xlsx', sheet_name='Sheet1', index = False)


#Locking the app behind a password
from pass_utility import check_credentials
# Do not continue if check_password is not True.  
# Main Streamlit app

#Setting page config
st.set_page_config(layout="centered")


# Main Streamlit App
if check_credentials():
    st.success("✅ Access granted!")
    # Add your main app logic here.
    st.write("Welcome to the app!")
else:
    st.warning("Please provide the correct credentials to proceed.")

    

#Add logo
add_logo("images/temp_logo.png", height=100)

#Add animatioon
path = "images/research_animation.json"
with open(path,"r") as file: 
    url = json.load(file) 

#CSS
st.markdown("""
<style>
.research {
    font-size: 100px;
    font-weight: bold;
    text-align: center;
    color: purple;
    display:inline;
}
            
.xpress {
    font-size: 100px;
    font-weight: bold;
    text-align: center;
    color: green;   
    display:inline;
}

.icon {
}
            
.element-container:has(#button-after) + div button {
 background-color: #6c757d;
 color: white;
 }
            
</style>
""", unsafe_allow_html=True)

#Title
st.markdown("<h1 style='text-align: center; padding-top: 0rem;'><p class='research'>research<p class='xpress'>Xpress</p></h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: Black;'>Synthesize Research Evidence through AI Capabilities</h4>", unsafe_allow_html=True)

#Animation
st_lottie(url, 
    loop=True, 
    quality='high',
    key='second'
    )
      
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3:
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
    get_started = st.button('Get Started', key = 'get_started')
    if get_started:
        switch_page("user guide")
