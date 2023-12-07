import requests
import logging
import time

# Setup logging
logging.basicConfig(filename='weather_data_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def fetch_weather_data(api_key, city):
    """
    Fetches real-time weather data from OpenWeatherMap API.
    Args:
        api_key (str): The API key for OpenWeatherMap.
        city (str): The name of the city for which to fetch weather data.
    Returns:
        dict: Weather data in JSON format, or None if an error occurs.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        logging.info("Weather data fetched successfully for {}".format(city))
        return data
    except requests.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as e:
        logging.error(f'Error occurred: {e}')

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API Key
    city = input("Please enter the name of the city: ")

    while True:
        weather_data = fetch_weather_data(api_key, city)
        if weather_data:
            print(weather_data)
        time.sleep(3600)  # Fetch data every hour -adjust for frequency

if __name__ == "__main__":
    main()

