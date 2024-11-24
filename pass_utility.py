# filename: utility.py
import streamlit as st  
import random  
import hmac  


import os
import openai
import streamlit as st
import hmac

# """  
# This file contains the common components used in the Streamlit App.  
# This includes the sidebar, the title, the footer, and the password check.  
# """  
  
  
def check_password():  
    """Returns `True` if the user had the correct password."""  
    def password_entered():  
        """Checks whether a password entered by the user is correct."""  
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):  
            st.session_state["password_correct"] = True  
            del st.session_state["password"]  # Don't store the password.  
        else:  
            st.session_state["password_correct"] = False  
    # Return True if the passward is validated.  
    if st.session_state.get("password_correct", False):  
        return True  
    # Show input for password.  
    st.text_input(  
        "Password", type="password", on_change=password_entered, key="password"  
    )  
    if "password_correct" in st.session_state:  
        st.error("😕 Password incorrect")  
    return False


def check_credentials():
    """Returns `True` if the user provided the correct password and API key."""
    def validate_password():
        """Checks whether the entered password is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    def validate_api_key():
        """Checks whether the entered OpenAI API key is valid."""
        try:
            openai.api_key = st.session_state["api_key"]
            openai.Engine.list()  # A simple API call to validate the key.
            os.environ['OPENAI_API_KEY'] = st.session_state["api_key"]
            st.session_state["api_key_correct"] = True
            del st.session_state["api_key"]  # Don't store the API key in plaintext.
        except Exception:
            st.session_state["api_key_correct"] = False

    # Check if both password and API key are validated.
    if st.session_state.get("password_correct", False) and st.session_state.get("api_key_correct", False):
        return True

    # Input for password.
    st.text_input("Password", type="password", on_change=validate_password, key="password")
    if st.session_state.get("password_correct") == False:
        st.error("😕 Password incorrect")

    # Input for OpenAI API key.
    st.text_input("OpenAI API Key", type="password", on_change=validate_api_key, key="api_key")
    if st.session_state.get("api_key_correct") == False:
        st.error("😕 Invalid OpenAI API Key")

    return False

   
import os
import openai
import streamlit as st

def validate_openai_api_key(api_key):
    """
    Validates the provided OpenAI API key by making a test request.
    Returns True if the key is valid, otherwise False.
    """
    try:
        openai.api_key = api_key
        openai.Model.list()  # Test request to validate the API key.
        return True
    except Exception as e:
        return False

def check_credentials():
    """Prompts the user for a password and OpenAI API key, and validates both."""
    def validate_inputs():
        """Validates the password and OpenAI API key."""
        # Validate password
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False
            return

        # Validate OpenAI API Key
        api_key = st.session_state["api_key"]
        if validate_openai_api_key(api_key):
            st.session_state["api_key_valid"] = True
            os.environ['OPENAI_API_KEY'] = api_key  # Store the API key
        else:
            st.session_state["api_key_valid"] = False

    # Check if both password and API key are validated
    if st.session_state.get("password_correct", False) and st.session_state.get("api_key_valid", False):
        return True

    # Prompt for password and API key
    st.text_input("Password", type="password", on_change=validate_inputs, key="password")
    st.text_input("OpenAI API Key", type="password", on_change=validate_inputs, key="api_key")

    # Display error messages
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 Password incorrect")
    if "api_key_valid" in st.session_state and not st.session_state["api_key_valid"]:
        st.error("😕 Invalid OpenAI API Key")

    return False


