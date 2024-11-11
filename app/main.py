from flask import Flask, render_template
from data_fetch import fetch_air_quality_data

app = Flask(__name__)

@app.route('/')
def home():
    city_name = "Portland"
    data, city_name = fetch_air_quality_data(45.5234, -122.6762, city_name)
    if data is not None:
        data = data.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
    return render_template('index.html', data=data, city_name=city_name)

if __name__ == '__main__':
    app.run(debug=True)
