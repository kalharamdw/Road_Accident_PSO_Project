import streamlit as st
import pandas as pd
from data_prep import load_and_clean_data
from risk_calculation import calculate_risk_score
from pso_model import run_pso_hotspot_ranking
from api_service import fetch_live_weather

st.title("AI-Based Road Accident Hotspot Analysis - Sri Lanka (All Districts)")
st.sidebar.header("Configuration & Filters")

# Load All Districts Data
df = load_and_clean_data()

# District Filter Selection
all_districts = sorted(df['District'].unique())
selected_district = st.sidebar.selectbox("Filter by District", ["All Districts"] + list(all_districts))

if selected_district != "All Districts":
    df_filtered = df[df['District'] == selected_district].copy()
    weather_city = selected_district
else:
    df_filtered = df.copy()
    weather_city = "Colombo"

# Live Environmental Feed Sidebar Widget
st.sidebar.header("Live Environmental Feed")
if st.sidebar.button("Fetch Live Weather Data"):
    with st.spinner("Fetching real-time updates..."):
        weather_data = fetch_live_weather(weather_city)
        if weather_data["Status"] == "Success":
            st.sidebar.success(f"Weather in {weather_data['City']}: {weather_data['Condition'].capitalize()}, {weather_data['Temperature (°C)']}°C")
        else:
            st.sidebar.error("Failed to load live data. Check API key.")

# 1. Dataset Overview
st.header("1. Nationwide Dataset Overview")
st.dataframe(df_filtered.head(100))

# 2. Risk Scores Calculation
df_risk = calculate_risk_score(df_filtered)

st.header("2. Risk Score Analysis by District/Location")
district_risk_summary = df_risk.groupby('District')['Risk_Score'].sum().reset_index()
st.bar_chart(district_risk_summary.set_index('District')['Risk_Score'])

# 3. Map Visualization
st.header("3. National Accident Hotspots Map")
map_df = df_risk.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
st.map(map_df[['lat', 'lon']])

# 4. PSO Prediction
st.header("4. PSO Hotspot Optimization Prediction")
if st.button("Run PSO Algorithm for High-Risk Hotspot"):
    hotspot_coords = run_pso_hotspot_ranking(df_risk)
    st.success(f"Algorithm Complete! Critical High-Risk Hotspot Identified at: Lat {hotspot_coords[0]:.4f}, Lon {hotspot_coords[1]:.4f}")
    pred_df = pd.DataFrame({'lat': [hotspot_coords[0]], 'lon': [hotspot_coords[1]]})
    st.map(pred_df)