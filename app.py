
import streamlit as st

st.title("Carte de suivi")
st.write("Ceci est une démo de Streamlit depuis Google Colab.")

name = st.text_input("Votre nom")
if name:
    st.write(f"Bonjour, {name} ! 👋")
