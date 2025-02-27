
import streamlit as st

st.title("Carte de suivi")
st.write("Ceci est une .")

name = st.text_input("Votre nom")
if name:
    st.write(f"Caca, {name} ! 👋")
