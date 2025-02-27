
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Analyse de Fichier Excel 📊")

# Chargement du fichier Excel
uploaded_file = st.file_uploader("Déposez votre fichier Excel ici", type=["xlsx", "xls"])

if uploaded_file:
    # Lire le fichier Excel dans un DataFrame pandas
    df = pd.read_excel(uploaded_file)

    # Afficher un aperçu des données
    st.subheader("Aperçu des données :")
    st.write(df.head())

    # Sélectionner une colonne numérique pour le graphe
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    
    if numeric_columns:
        column = st.selectbox("Choisissez une colonne pour le graphe", numeric_columns)

        # Générer le graphe
        fig, ax = plt.subplots()
        ax.plot(df[column], marker='o', linestyle='-')
        ax.set_title(f"Évolution de {column}")
        ax.set_xlabel("Index")
        ax.set_ylabel(column)

        # Afficher le graphe dans Streamlit
        st.pyplot(fig)
    else:
        st.warning("Aucune colonne numérique détectée dans le fichier Excel.")

