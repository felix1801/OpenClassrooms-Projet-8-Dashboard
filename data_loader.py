# data_loader.py
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    # Simulons des données pour l'exemple
    data = pd.DataFrame({
        'SK_ID_CURR': np.random.randint(100000, 999999, 1000),
        'PAYMENT_RATE': np.random.uniform(0, 1, 1000),
        'EXT_SOURCE_3': np.random.uniform(0, 1, 1000), 
        'EXT_SOURCE_2': np.random.uniform(0, 1, 1000),
        'DAY_BIRTH': np.random.randint(18, 70, 1000),
        'EXT_SOURCE_1': np.random.uniform(0, 1, 1000),
        'DAYS_EMPLOYED': np.random.randint(-20000, 0, 1000),
        'DAYS_EMPLOYED_PERC': np.random.uniform(0, 1, 1000),
        'DAYS_REGISTRATION': np.random.randint(-2000, 0, 1000),
        'DAYS_ID_PUBLISH': np.random.randint(-2000, 0, 1000),
        'ANNUITY_INCOME_PERC': np.random.uniform(0, 1, 1000),
        'INSTAL_DBD_MEAN': np.random.uniform(0, 1, 1000),
        'AMT_ANNUITY': np.random.randint(5000, 50000, 1000),
    })
    return data