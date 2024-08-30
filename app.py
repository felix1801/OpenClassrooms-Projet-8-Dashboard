# streamlit allows to create a web application with python.
# app.py is the main page of the web application.
import streamlit as st

# Load secrets API_URL (heroku.myAPI) and API_KEY (azertyuiop123...)
api_url = st.secrets["API_URL"]
api_key = st.secrets["API_KEY"]

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

def main():
    st.set_page_config(page_title="Dashboard de Scoring Crédit", layout="wide")
    
    data = load_data()
    
    st.sidebar.title("Sélection du client")
    client_id = st.sidebar.selectbox("ID du client", data['client_id'])
    
    client_data = data[data['client_id'] == client_id].iloc[0]
    
    st.title(f"Dashboard du client {client_id}")
    
    col1, col2 = st.columns(2)
    with col1:
        plot_client_info(client_data)
    
    with col2:
        score, probability = predict_score(client_data)
        plot_score_probability(score, probability)
    
    st.subheader("Comparaison avec l'ensemble des clients")
    feature_to_compare = st.selectbox("Choisissez une caractéristique à comparer", config.FEATURES)
    plot_feature_comparison(data, client_data, feature_to_compare)
    
    st.subheader("Analyse bivariée")
    x_axis = st.selectbox("Choisissez la caractéristique pour l'axe X", config.FEATURES)
    y_axis = st.selectbox("Choisissez la caractéristique pour l'axe Y", config.FEATURES)
    plot_bivariate_analysis(data, client_data, x_axis, y_axis)
    
    st.subheader("Modifier les informations du client")
    updated_data = update_client_data(client_data)
    if st.button("Mettre à jour et recalculer le score"):
        new_score, new_probability = predict_score(updated_data)
        st.write(f"Nouveau score: {'Accepté' if new_score == 1 else 'Refusé'}")
        st.write(f"Nouvelle probabilité: {new_probability:.2f}")
    
    st.subheader("Ajouter un nouveau client")
    new_client_data = create_new_client()
    if st.button("Calculer le score pour le nouveau client"):
        new_client_score, new_client_probability = predict_score(new_client_data)
        st.write(f"Score du nouveau client: {'Accepté' if new_client_score == 1 else 'Refusé'}")
        st.write(f"Probabilité du nouveau client: {new_client_probability:.2f}")
    
    st.markdown(config.ACCESSIBILITY_FOOTER, unsafe_allow_html=True)

if __name__ == "__main__":
    main()