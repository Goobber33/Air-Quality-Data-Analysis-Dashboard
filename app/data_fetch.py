import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/air_pollution"

def fetch_air_quality_data(lat, lon):
    response = requests.get(
        f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
    )
    data = response.json()
    print(data)  # Print the response to inspect its structure

    # Check if 'list' key is present in the response
    if 'list' not in data:
        raise KeyError("'list' key not found in the API response. Response:", data)

    # Convert to DataFrame if 'list' is present
    df = pd.DataFrame(data['list'])
    return df
