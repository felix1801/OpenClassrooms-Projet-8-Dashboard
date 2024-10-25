import streamlit as st
import pandas as pd
import config

def update_client_data(client_data):
    updated_data = client_data.copy()
    for feature in config.FEATURES:
        updated_data[feature] = st.number_input(f"Nouveau {feature}", min_value=float(-1000000), max_value=float(1000000), value=client_data[feature])
    return updated_data

def create_new_client():
    new_client_data = {}
    for feature in config.FEATURES:
        new_client_data[feature] = st.number_input(f"{feature} du nouveau client", min_value=float(-1000000), max_value=float(1000000))
    return pd.Series(new_client_data)
