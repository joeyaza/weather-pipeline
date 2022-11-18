import requests

def get_location_key(location, api_key): 

    try:
        method = "get"
        url = f'http://dataservice.accuweather.com/locations/v1/cities/se/search?q={location}&apikey={api_key}'
        response = requests.request(method, url)
        if response.status_code == 200:
            location_response = response.json()[0]
            location_key = location_response["Key"]
            return location_key
        else: 
            raise RuntimeError(f"Location key not retrieved: please see error code {response.status_code}")
    except requests.exceptions.HTTPError as err:
        raise RuntimeError(str(err))
