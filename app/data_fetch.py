import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/air_pollution"

def fetch_air_quality_data(city, country):
    response = requests.get(
        f"{BASE_URL}?q={city},{country}&appid={API_KEY}"
    )
    data = response.json()
    # Convert to DataFrame for processing
    df = pd.DataFrame(data['list'])
    return df
