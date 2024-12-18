import requests
import streamlit as st

# Load secrets API_URL (heroku.myAPI)
# API_URL = "http://127.0.0.1:5000" # Local API and local dashboard run
API_URL = "https://openclassrooms-projet-7-api-d1ec900c726b.herokuapp.com/" # Remote API but local dashboard run

# Fonction pour appeler l'API de scoring avec les données du client
def predict_score(client_data):
    response = requests.post(f"{API_URL}/predict", json=client_data)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Erreur lors de l'appel à l'API")
        return None