import pandas as pd
import streamlit as st
import plotly.express as px

def plot_client_info(client_data):
    st.subheader("Informations du client")
    for feature, value in client_data.items():
        if feature != 'client_id':
            st.write(f"{feature.capitalize()}: {value}")


def plot_score_probability(score, probability, threshold):
    st.subheader("Aide à la décision et probabilité de défaut de paiement")
    
    # Affichage de la décision de prêt
    st.metric("Prêt", "Accepté" if score == 0 else "Refusé")
    
    # Calcul de la largeur de la barre de progression et du seuil
    progress_width = int(probability * 100)
    threshold_width = int(threshold * 100)
    
    # Choix de la couleur en fonction du seuil
    if probability <= threshold:
        progress_color = "green"
    else:
        progress_color = "red"
    
    # Barre de progression personnalisée
    st.markdown(f"""
    <div style="width:100%; background-color:#e0e0e0; border-radius:10px;position:relative;height:30px;">
        <!-- Barre de progression -->
        <div style="width:{progress_width}%; 
                    background-color:{progress_color}; 
                    height:30px; 
                    border-radius:10px; 
                    position:absolute; 
                    top:0; 
                    left:0;">
        </div>
        <!-- Marqueur de seuil -->
        <div style="width:4px; 
                    background-color:black; 
                    height:40px; 
                    position:absolute; 
                    top:-5px; 
                    left:{threshold_width}%; 
                    z-index:10;">
        </div>
        <!-- Texte de progression -->
        <div style="width:100%; 
                    height:30px; 
                    position:absolute; 
                    top:0; 
                    left:0; 
                    display:flex; 
                    justify-content:center; 
                    align-items:center; 
                    color:white; 
                    font-weight:bold;">
            {probability:.2%}
        </div>
        
        
    </div>
    """, unsafe_allow_html=True)
    
    # Affichage textuel de la probabilité et du seuil
    st.write("Probabilité de défaut de paiement")
    st.write(f"Seuil : {threshold:.0%}")

def plot_feature_comparison(data, client_data, feature):
    fig = px.histogram(data, x=feature, nbins=30)
    fig.add_vline(x=client_data[feature], line_dash="dash", line_color="red")
    st.plotly_chart(fig)

def plot_bivariate_analysis(data, client_data, x_axis, y_axis):
    fig = px.scatter(data, x=x_axis, y=y_axis, opacity=0.6)
    fig.add_trace(px.scatter(pd.DataFrame([client_data]), x=x_axis, y=y_axis, 
                             color_discrete_sequence=['red']).data[0])
    st.plotly_chart(fig)
