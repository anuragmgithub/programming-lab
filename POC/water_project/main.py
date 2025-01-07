import logging
from logging_config import setup_logging
from weather_app.fetcher import fetch_weather_data

def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        city = input("Enter city name to fetch weather: ").strip()
        weather_data = fetch_weather_data(city)
        logger.info("Weather data fetched successfully: %s", weather_data)
    except Exception as e:
        logger.error("Error occurred: %s", e)

if __name__ == "__main__":
    main()
