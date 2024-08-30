import streamlit as st
import plotly.express as px

def plot_client_info(client_data):
    st.subheader("Informations du client")
    for feature, value in client_data.items():
        if feature != 'client_id':
            st.write(f"{feature.capitalize()}: {value}")

def plot_score_probability(score, probability):
    st.subheader("Score et Probabilité")
    st.metric("Score", "Accepté" if score == 1 else "Refusé")
    st.progress(probability)
    st.write(f"Probabilité: {probability:.2f}")

def plot_feature_comparison(data, client_data, feature):
    fig = px.histogram(data, x=feature, nbins=30)
    fig.add_vline(x=client_data[feature], line_dash="dash", line_color="red")
    st.plotly_chart(fig)

def plot_bivariate_analysis(data, client_data, x_axis, y_axis):
    fig = px.scatter(data, x=x_axis, y=y_axis, opacity=0.6)
    fig.add_trace(px.scatter(pd.DataFrame([client_data]), x=x_axis, y=y_axis, 
                             color_discrete_sequence=['red']).data[0])
    st.plotly_chart(fig)
