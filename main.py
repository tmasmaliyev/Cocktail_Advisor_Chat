import streamlit as st
import requests

st.title("The Cocktail Advisor Chat")

with st.form("my_form"):
    text = st.text_input("Enter some text")
    submitted = st.form_submit_button("Submit")

if submitted:
    url = "http://127.0.0.1:5000/submit"
    data = {"text": text}
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            st.success(f"Response: {response.json()['result']}")
        else:
            st.error(f"Error: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Failed to connect to the backend. Make sure it's running!")