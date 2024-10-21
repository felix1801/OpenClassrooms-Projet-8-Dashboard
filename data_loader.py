# data_loader.py
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data(data_path):
    # Simulons des données pour l'exemple
    data = pd.read_csv(data_path)
    return data