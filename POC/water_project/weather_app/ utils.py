import logging

logger = logging.getLogger(__name__)

def validate_city_name(city: str):
    """Validate the city name input."""
    if not city or not city.isalpha():
        logger.error("Invalid city name: %s", city)
        raise ValueError("City name must only contain alphabetic characters.")
    logger.debug("City name validation passed: %s", city)
