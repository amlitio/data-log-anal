import requests
import logging

# Setup console logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def fetch_weather_data(api_key, zip_code, country_code):
    """Fetches current weather data using OpenWeatherMap API 2.5."""
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'zip': f'{zip_code},{country_code}',
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return None

def display_weather_info(weather_data, zip_code):
    """Display weather information in a user-friendly format."""
    weather = weather_data['weather'][0]['description'].title()
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"\nCurrent Weather for ZIP Code {zip_code}:")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} meter/sec\n")

def main():
    api_key = 'your_api_key'  # Replace with your OpenWeatherMap API Key
    zip_code = input("Please enter the zip code: ")
    country_code = input("Please enter the country code: ")
    weather_data = fetch_weather_data(api_key, zip_code, country_code)

    if weather_data:
        display_weather_info(weather_data, zip_code)
    else:
        logging.error("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
