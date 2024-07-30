import streamlit as st

st.header("Contact me")

with st.form(key = "email_form"):
    user_email = st.text_input("Email Address")
    message = st.text_area("Message")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        print("Button pressed")