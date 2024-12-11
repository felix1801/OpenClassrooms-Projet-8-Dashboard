import streamlit as st

from data_loader import load_data
from model import predict_score
from visualization import (
    plot_client_info,
    plot_score_probability,
    plot_feature_comparison,
    plot_bivariate_analysis
)
from utils import update_client_data, create_new_client
import config

import os
import numpy as np
import pandas as pd

def main():
    import streamlit as st
import os
import pandas as pd
import config

st.set_page_config(page_title="Dashboard de Scoring Crédit", layout="wide")

data_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'OpenClassrooms-Projet-7', 'modeling', 'data', '04_feature', 'test_features.csv'))

data = load_data(data_path)

st.sidebar.title("Sélection du client")
client_id = st.sidebar.selectbox("ID du client", data['SK_ID_CURR'])

client_index = data[data['SK_ID_CURR'] == client_id].index[0]
client_data = data.iloc[client_index]

# Création des onglets
tab_client, tab_analyse, tab_modifier, tab_nouveau = st.tabs([
    "Client", 
    "Analyse", 
    "Modifier les données du client", 
    "Créer un nouveau client"
])

# Onglet Client
with tab_client:
    st.title(f"Fiche du client n°{client_id}")
    col1, col2 = st.columns(2)

    with col1:
        plot_client_info(client_data)
    
    with col2:
        for col in config.FEATURES:
            if pd.isna(client_data[col]):
                client_data[col] = data[col].mean()
    
        result = predict_score([client_data.to_dict()])
        score = result['scores'][0]
        probability = result['probas'][0]
        threshold = result['thresholds'][0]
        plot_score_probability(score, probability, threshold)

# Onglet Analyse
with tab_analyse:
    st.subheader("Comparaison avec l'ensemble des clients")
    feature_to_compare = st.selectbox("Choisissez une caractéristique à comparer", config.FEATURES)
    plot_feature_comparison(data, client_data, feature_to_compare)
    
    st.subheader("Analyse bivariée")
    x_axis = st.selectbox("Choisissez la caractéristique pour l'axe X", config.FEATURES)
    y_axis = st.selectbox("Choisissez la caractéristique pour l'axe Y", config.FEATURES)
    plot_bivariate_analysis(data, client_data, x_axis, y_axis)

# Onglet Modifier les données du client
with tab_modifier:
    st.subheader("Modifier les informations du client")
    updated_client_data = update_client_data(client_data)
    if st.button("Mettre à jour et recalculer le score"):
        update_client_data_list = [updated_client_data.to_dict()]
        
        new_result = predict_score(update_client_data_list)
        new_score = new_result['scores'][0]
        new_probability = new_result['probas'][0]        

        st.subheader("Nouvelle prédiction:")
        plot_score_probability(new_score, new_probability, threshold)

# Onglet Créer un nouveau client
with tab_nouveau:
    st.subheader("Ajouter un nouveau client")
    new_client_data = create_new_client(data.mean())
    if st.button("Calculer le score pour le nouveau client"):
        new_client_data_list = [new_client_data.to_dict()]
        
        new_client_result = predict_score(new_client_data_list)
        new_client_score = new_client_result['scores'][0]
        new_client_probability = new_client_result['probas'][0]        

        st.subheader("Prédiction du nouveau client :")
        plot_score_probability(new_client_score, new_client_probability, threshold)

st.markdown(config.ACCESSIBILITY_FOOTER, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# TO DO :
# - [X] Pour nouveau client, mettre les valeurs moyenne par défaut
# - [X] Visualisation du score de crédit (jauge colorée) - seuil fait le changement de couleur
# - [X] Joli design
#   