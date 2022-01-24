import pandas as pd
import streamlit as st
from league_data import download_league_data, download_free_agents

st.set_page_config(
   page_title="Dub Dynasty",
   page_icon=":basketball:",
   layout="wide",
   initial_sidebar_state="expanded",
)

hide_st_style = """
<style> 
footer {visibility: hidden;}
[data-testid="stDecoration"] {visibility: hidden;}
[class="block-container css-18e3th9 egzxvld2"] {padding: 1rem 4rem 6rem}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)



st.title(':basketball:  Dub Dynasty')

# Download Buttons
b_col_1, b_col_2, _,_,_ = st.columns(5)
with b_col_1:
    download_league = st.button('Update League Data')
    if download_league:
        download_league_data()
    # st.write('')
with b_col_2:
    download_fa = st.button('Update Free Agent Data')
    if download_fa:
        download_free_agents()
    # st.write('')

# Free Agent Data
st.write('')
st.subheader('Free Agents')

fa = pd.read_csv('free_agents.csv')

# filters
columns = st.multiselect('Filter Columns', options=fa.columns)
if columns:
    fa = fa[columns]

# n_col_1, n_col_2, n_col_3, n_col_4, n_col_5, n_col_6 = st.columns(6)
# with n_col_1:
#     min_gp = st.number_input('Min. GP', min_value=0, value=0, step=1, disabled=True)
    
# TODO - add filter for injured



# TODO - update to only do this if the filters are set



st.dataframe(data=fa)








# hide_st_style = """
# <style>
# footer {visibility: hidden;}
# [data-testid="stDecoration"] {visibility: hidden;}
# [class="block-container"] {padding: 1rem 2rem 6rem}
# </style>
# """

# # st.markdown(hide_st_style, unsafe_allow_html=True)

# hide_footer_style = """
# <style>
# .reportview-container .main footer {visibility: hidden;}  
# </style>  
# """
# st.markdown(hide_footer_style, unsafe_allow_html=True)