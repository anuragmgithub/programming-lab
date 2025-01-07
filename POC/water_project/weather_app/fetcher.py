import logging
import requests
from weather_app.utils import validate_city_name

API_KEY = "your_openweathermap_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

logger = logging.getLogger(__name__)

def fetch_weather_data(city: str):
    """Fetch weather data for a given city."""
    logger.debug("Validating city name: %s", city)
    validate_city_name(city)

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    logger.info("Sending request to weather API for city: %s", city)
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        logger.error("API request failed with status code: %d", response.status_code)
        raise Exception(f"Failed to fetch weather data: {response.text}")

    logger.debug("Weather API response received: %s", response.json())
    return response.json()
