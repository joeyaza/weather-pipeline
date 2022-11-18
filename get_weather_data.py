import requests
import logging
import json
from utils import construct_record_name

def get_weather_data(location, location_key, api_key):
    try:
        method = "get"
        url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}'
        response = requests.request(method, url)
        if response.status_code == 200:
            location_weather = response.json()[0]
            date_time = location_weather["LocalObservationDateTime"]
            year = date_time[:4]
            month = date_time[5:7]
            day = date_time[8:10]
            hour = date_time[11:13]
            logging.info(f'Weather data returned for {location}, {year}-{month}-{day}')
            DTO = {
                "location": location,
                "summary": location_weather['WeatherText'],
                "has_precipitation": location_weather["HasPrecipitation"],
                "temperature": location_weather["Temperature"]["Metric"]["Value"],
                "year": year,
                "month": month,
                "day": day,
                "hour": hour
            }
            return DTO
        else: 
            raise RuntimeError(f"Location key not retrieved: please see error code {response.status_code}")
    except requests.exceptions.HTTPError as err:
        raise RuntimeError(str(err))


