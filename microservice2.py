from flask import Flask, jsonify
import requests

app = Flask(__name__)
@app.route('/weather/<zip_code>', methods=['GET'])
def get_weather(zip_code):
    api_key = 'ed3112cc82e403310c0dd19c54b68137'
    url = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}'
    #check address http://localhost:8000/weather/94539
    response = requests.get(url)
    weather_data = response.json()
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)