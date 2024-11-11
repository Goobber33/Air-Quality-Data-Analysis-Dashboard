from flask import Flask, render_template, request, redirect, url_for
from data_fetch import fetch_air_quality_data
import requests
import os

app = Flask(__name__)
GEO_API_URL = "http://api.openweathermap.org/geo/1.0/direct"
API_KEY = os.getenv('API_KEY')

@app.route('/', methods=['GET', 'POST'])
def home():
    city_name = "Portland"
    if request.method == 'POST':
        city_name = request.form.get('city')

        # Fetch latitude and longitude for the city

        geo_response = requests.get(f"{GEO_API_URL}?q={city_name}&limit=1&appid={API_KEY}")
        geo_data = geo_response.json()

        if geo_data:
            lat = geo_data[0]['lat']
            lon = geo_data[0]['lon']
            data, city_name = fetch_air_quality_data(lat, lon, city_name)
            data = data.to_dict(orient='records') if data is not None else []
            return render_template('index.html', data=data, city_name=city_name)

    # Default Portland air quality if no search
    
    data, city_name = fetch_air_quality_data(45.5234, -122.6762, city_name)
    data = data.to_dict(orient='records') if data is not None else []
    return render_template('index.html', data=data, city_name=city_name)

if __name__ == '__main__':
    app.run(debug=True)
