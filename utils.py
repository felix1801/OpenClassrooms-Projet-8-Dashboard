import streamlit as st
import pandas as pd
import config

def update_client_data(client_data):
    updated_data = client_data.copy()
    for feature in config.FEATURES:
        if feature == 'CODE_GENDER' or feature == 'NAME_EDUCATION_TYPE_Highereducation':
            updated_data[feature] = st.selectbox(f"Nouveau {feature}", options=[0, 1], index=0)
        else:
            updated_data[feature] = st.number_input(f"Nouveau {feature}", min_value=float(-1000000), max_value=float(1000000), value=float(client_data[feature]))
    return updated_data

def create_new_client(mean_values):
    new_client_data = {}
    for feature in config.FEATURES:
        if feature == 'CODE_GENDER' or feature == 'NAME_EDUCATION_TYPE_Highereducation':
            new_client_data[feature] = st.selectbox(f"{feature} du nouveau client", options=[0, 1], index=0)
        else:
            new_client_data[feature] = st.number_input(f"{feature} du nouveau client", min_value=float(-1000000), max_value=float(1000000), value=mean_values[feature])
    return pd.Series(new_client_data)


