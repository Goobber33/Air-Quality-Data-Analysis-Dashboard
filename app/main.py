from flask import Flask, render_template
from data_fetch import fetch_air_quality_data

app = Flask(__name__)

@app.route('/')
def home():
    data = fetch_air_quality_data(45.5234, -122.6762)  # Latitude and longitude for Portland, OR
    if data is not None:
        data = data.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
