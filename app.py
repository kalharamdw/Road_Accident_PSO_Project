import streamlit as st
import pandas as pd
from data_prep import load_and_clean_data
from risk_calculation import calculate_risk_score
from pso_model import run_pso_hotspot_ranking
from api_service import fetch_live_weather

st.title("AI-Based Road Accident Hotspot Analysis - Sri Lanka")
st.sidebar.header("Configuration")

# Live Data Integration Section
st.sidebar.header("Live Environmental Feed")
selected_city = st.sidebar.selectbox("Select District for Live Weather", ["Colombo", "Gampaha", "Kandy", "Galle"])

if st.sidebar.button("Fetch Live Weather Data"):
    with st.spinner("Fetching real-time updates..."):
        weather_data = fetch_live_weather(selected_city)
        if weather_data["Status"] == "Success":
            st.sidebar.success(f"Weather in {weather_data['City']}: {weather_data['Condition'].capitalize()}, {weather_data['Temperature (°C)']}°C")
        else:
            st.sidebar.error("Failed to load live data. Check API key.")

# 1. Load Data
st.header("1. Dataset Overview")
df = load_and_clean_data("dummy.csv")
st.dataframe(df)

# 2. Risk Scores
st.header("2. Risk Score Analysis")
df_risk = calculate_risk_score(df)
st.bar_chart(df_risk.set_index('District')['Risk_Score'])

# 3. Map Visualization
st.header("3. Accident Locations")
map_df = df_risk.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
st.map(map_df[['lat', 'lon']])

# 4. PSO Prediction
st.header("4. PSO Hotspot Prediction")
if st.button("Run PSO Algorithm"):
    hotspot_coords = run_pso_hotspot_ranking(df_risk)
    st.success(f"Algorithm Complete! High-Risk Hotspot Identified at: Lat {hotspot_coords[0]:.4f}, Lon {hotspot_coords[1]:.4f}")
    pred_df = pd.DataFrame({'lat': [hotspot_coords[0]], 'lon': [hotspot_coords[1]]})
    st.map(pred_df)