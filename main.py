import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="Weather App",
    page_icon="🌦️",
    layout="centered"
)

# Title
st.title("🌦️ Weather Forecast App")

st.write("Enter a city name and get live weather information.")

# API Key
# API_KEY = "YOUR_API_KEY"
API_KEY = st.secrets["OPENWEATHER_API_KEY"]

# Input
city = st.text_input("Enter City Name")

# Button
if st.button("Get Weather"):

    if city:

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:

                data = response.json()

                city_name = data["name"]
                country = data["sys"]["country"]
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind_speed = data["wind"]["speed"]
                condition = data["weather"][0]["main"]
                description = data["weather"][0]["description"]

                st.success("Weather Data Retrieved Successfully")

                st.subheader(f"📍 {city_name}, {country}")

                st.metric("🌡️ Temperature", f"{temp} °C")
                st.metric("💧 Humidity", f"{humidity}%")

                st.write(f"**☁️ Condition:** {condition}")
                st.write(f"**📝 Description:** {description}")
                st.write(f"**🌬️ Wind Speed:** {wind_speed} m/s")
                st.write(f"**📊 Pressure:** {pressure} hPa")

            elif response.status_code == 404:
                st.error("City not found")

            else:
                st.error("Something went wrong")

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a city name")