import logging
import sys
from convert_to_avro import convert_to_avro
from get_location_key import get_location_key
from get_weather_data import get_weather_data
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level = logging.INFO)
logging.info('Process started')

api_key = os.environ.get("accuweather-api-key")
location = sys.argv[1]
logging.info(f'Getting location key for: {location}')
location_key = get_location_key(location, api_key)
logging.info(f'Location key: {location_key} for: {location} retrieved')
weather_data = get_weather_data(location, location_key, api_key)
convert_to_avro(weather_data)
