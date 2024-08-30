import streamlit as st
import pandas as pd
import config

def update_client_data(client_data):
    updated_data = client_data.copy()
    for feature in config.FEATURES:
        if feature == 'debt_ratio':
            updated_data[feature] = st.number_input(f"Nouveau {feature}", min_value=0.0, max_value=1.0, value=client_data[feature])
        else:
            updated_data[feature] = st.number_input(f"Nouveau {feature}", min_value=0, max_value=1000000, value=client_data[feature])
    return updated_data

def create_new_client():
    new_client_data = {}
    for feature in config.FEATURES:
        if feature == 'debt_ratio':
            new_client_data[feature] = st.number_input(f"{feature} du nouveau client", min_value=0.0, max_value=1.0)
        else:
            new_client_data[feature] = st.number_input(f"{feature} du nouveau client", min_value=0, max_value=1000000)
    return pd.Series(new_client_data)
