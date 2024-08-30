import requests
import streamlit as st

# Load secrets API_URL (heroku.myAPI)
API_URL = st.secrets["API_URL"]

# Fonction pour appeler l'API de scoring avec les données du client
def predict_score(client_data):
    response = requests.post(f"{API_URL}/predict", json=client_data)
    if response.status_code == 200:
        data = response.json()
        return data['score'], data['probability']
    else:
        st.error("Erreur lors de l'appel à l'API")
        return None, None