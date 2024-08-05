from loguru import logger
import os
import streamlit as st
import streamlit_extras.app_logo as app_logo
from streamlit_extras.badges import badge
from htbuilder import a, img
from streamlit_extras.stylable_container import stylable_container
from streamlit.source_util import (
    get_pages,
    _on_pages_changed,
    invalidate_pages_cache,
)

def change_mode_pages(mode):
    main_script_path = os.path.abspath('../Home.py')
    invalidate_pages_cache()
    all_pages = get_pages(main_script_path)
    if mode == "Creator":
        pages = ['Home', 'Workspace', "My_Apps"]
    else:
        pages = ['Home', "My_Apps"]
    logger.info(f"pages: {pages}, mode: {mode}")

    current_pages = [key for key, value in all_pages.items() if value['page_name'] not in pages]
    for key in current_pages:
        all_pages.pop(key)
            
    _on_pages_changed.send()

def init_env_default():
    # init env default
    if 'MODE' in st.secrets:
        os.environ.setdefault('MODE', st.secrets['MODE'])
        
    if 'COMFYFLOW_API_URL' in st.secrets:
        os.environ.setdefault('COMFYFLOW_API_URL', st.secrets['COMFYFLOW_API_URL'])
    if 'COMFYUI_SERVER_ADDR' in st.secrets:
        os.environ.setdefault('COMFYUI_SERVER_ADDR', st.secrets['COMFYUI_SERVER_ADDR'])
    
    if 'DISCORD_CLIENT_ID' in st.secrets:
        os.environ.setdefault('DISCORD_CLIENT_ID', st.secrets['DISCORD_CLIENT_ID'])
    if 'DISCORD_CLIENT_SECRET' in st.secrets:
        os.environ.setdefault('DISCORD_CLIENT_SECRET', st.secrets['DISCORD_CLIENT_SECRET'])
    if 'DISCORD_REDIRECT_URI' in st.secrets:
        os.environ.setdefault('DISCORD_REDIRECT_URI', st.secrets['DISCORD_REDIRECT_URI'])

def page_init(layout="wide"):
    """
    mode, studio or creator
    """
    st.set_page_config(
        page_title="UltimateAI: Image Generation", 
        page_icon=":artist:", 
        layout=layout,
        initial_sidebar_state="collapsed",
        menu_items=None
    )

    change_mode_pages(os.environ.get('MODE'))

    #app_logo.add_logo("public/images/logo.png", height=70)

    # reduce top padding and remove sidebar
    st.markdown("""
            <style>
                .block-container {
                        padding-top: 1rem;
                        padding-bottom: 0rem;
                    }
                [data-testid="stSidebar"] {display: none;}
                div[data-testid="stToolbar"] {display: none;}
                div[data-testid="stDecoration"] {display: none;}
                div[data-testid="stStatusWidget"] {display: none;}
            </style>
            """, unsafe_allow_html=True)
    
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            div[data-testid="stSidebarNav"] {display: none;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def stylable_button_container():
    return stylable_container(
        key="app_button",
        css_styles="""
            button {
                background-color: rgb(28 131 225);
                color: white;
                border-radius: 4px;
                width: 120px;
            }
            button:hover, button:focus {
                border: 0px solid rgb(28 131 225);
            }
        """,
    )

def exchange_button_container():
    return stylable_container(
        key="exchange_button",
        css_styles="""
            button {
                background-color: rgb(28 131 225);
                color: white;
                border-radius: 4px;
                width: 200px;
            }
            button:hover, button:focus {
                border: 0px solid rgb(28 131 225);
            }
        """,
    )

def custom_text_area():
    custom_css = """
            <style>
            textarea {
                height: auto;
                max-height: 250px;
            }
            </style>
        """
    st.markdown(custom_css, unsafe_allow_html=True)