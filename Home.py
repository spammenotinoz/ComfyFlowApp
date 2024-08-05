import streamlit as st
import os
from streamlit.source_util import get_pages
from loguru import logger
from streamlit_extras.row import row
from modules import page
from modules.authenticate import MyAuthenticate

def redirect_to_my_apps():
    logger.info("Redirecting to My_Apps")
    st.switch_page("pages/My_Apps.py")

page.init_env_default()
page.page_init(layout="centered")

# Check for the environment variable at the start
should_redirect = os.environ.get('REDIRECT_TO_MY_APPS', '').lower() == 'true'

auth_instance = MyAuthenticate("comfyflow_token", "ComfyFlowApp： Load ComfyUI workflow as webapp in seconds.")

with st.container():
    header_row = row([0.87, 0.13], vertical_align="bottom")
    header_row.title("Welcome")
    header_button = header_row.empty()  

    if not st.session_state.get('authentication_status'):
        with st.container():
            st.markdown("Image Generation")
            auth_instance.login("Login")
            # Check if login was successful
            if st.session_state.get('authentication_status'):
                st.rerun()  # Rerun to update the page after successful login
    else: 
        with header_button:
            auth_instance.logout(button_name="Logout", location="main", key="home_logout_button")
        
        with st.container():
            name = st.session_state['name']
            username = st.session_state['username']
            st.markdown(f"Hello, {name}({username}) :smile:")
        
        # Only redirect if authenticated and redirection is requested
        if should_redirect:
            logger.info("User is authenticated and redirection is requested")
            redirect_to_my_apps()

logger.info(f"Current page: {st.session_state.get('current_page', 'Unknown')}")
logger.info(f"Authentication status: {st.session_state.get('authentication_status', False)}")