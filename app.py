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

b_col_1, b_col_2, _,_,_,_ = st.columns(6)

with b_col_1:
    st.button('Update League Data', on_click=download_league_data())
with b_col_2:
    st.button('Update Free Agent Data', on_click=download_free_agents())

st.write('')
st.subheader('Free Agents')
fa = pd.read_csv('free_agents.csv')
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