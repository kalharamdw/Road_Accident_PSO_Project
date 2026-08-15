import requests
import streamlit as st

def fetch_live_weather(city="Colombo"):
    """
    Fetches live weather data using the API key stored in Streamlit secrets.
    This correlates with accident causes like unfavourable weather.
    """
    try:
        # Retrieve API key securely from Streamlit secrets
        api_key = st.secrets["WEATHER_API_KEY"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},LK&appid={api_key}&units=metric"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_condition = data['weather'][0]['description']
            temperature = data['main']['temp']
            return {
                "City": city,
                "Condition": weather_condition,
                "Temperature (°C)": temperature,
                "Status": "Success"
            }
        else:
            return {"Status": "Error", "Message": "Could not fetch live data"}
    except Exception as e:
        return {"Status": "Error", "Message": str(e)}