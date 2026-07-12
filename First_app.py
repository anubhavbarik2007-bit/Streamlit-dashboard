import streamlit as st

st.title("My First Streamlit app")
st.write("Hello my app is running successfully")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Welcome {name}!")
