import pytest
from weather_app.fetcher import fetch_weather_data

def test_fetch_weather_data():
    """Test fetching weather data."""
    # Replace 'test_city' with a real city for actual testing
    city = "London"
    data = fetch_weather_data(city)
    assert "main" in data  # Assuming the 'main' field is present in API response
