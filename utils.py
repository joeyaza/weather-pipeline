def construct_record_name(weather_data):
    return f'weather-record-{weather_data["location"]}-{weather_data["year"]}-{weather_data["month"]}-{weather_data["day"]}'