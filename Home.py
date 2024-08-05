import streamlit as st
import requests
import os
from loguru import logger
from streamlit_authenticator.exceptions import RegisterError
from streamlit_extras.row import row
from modules import page
from modules.authenticate import MyAuthenticate
from modules.authenticate import Validator


def gen_invite_code(source: str, uid: str):
    invate_code = f"oauth_{source}_{uid}"
    return invate_code
    
def back_home_signup():
    st.session_state.pop('user_data', None)
    logger.info("back home login")

page.init_env_default()
page.page_init(layout="centered")

with st.container():
    header_row = row([0.87, 0.13], vertical_align="bottom")
    header_row.title("""
        Welcome       
    """)
    header_button = header_row.empty()  

    auth_instance =  MyAuthenticate("comfyflow_token", "ComfyFlowApp： Load ComfyUI workflow as webapp in seconds.")
    if not st.session_state['authentication_status']:
        
        with st.container():
            try:
                st.markdown("Image Generation")
                auth_instance.login("Login")
            except Exception as e:  
                st.error(f"Login failed, {e}")
        
    else: 
        with header_button:
            auth_instance.logout(button_name="Logout", location="main", key="home_logout_button")

        
        with st.container():
            name = st.session_state['name']
            username = st.session_state['username']
            st.markdown(f"Hello, {name}({username}) :smile:")         
