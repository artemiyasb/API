from datetime import datetime    #модуль для работы со временем
from flask import Flask, jsonify
import pytz                     #модуль для работы с часовыми поясами
from pytz import timezone       #модуль для работы

app = Flask(__name__)

@app.route('/time')

def get_time():
    nyc = timezone('America/New_York')
    nyc_time = datetime.now(nyc)
    return str(nyc_time)

@app.route("/cities", methods = ["GET"])
def get_cities():
    cities = [
        {"name": "Yerevan", "population": 1075800},
        {"name": "Gyumri", "population": 117000},
        {"name": "Vanadzor", "population": 82200},
        {"name": "Masis", "population": 20500},
        {"name": "Goris", "population": 20300},
        {"name": "Hrazdan", "population": 41200},
        {"name": "Kapan", "population": 42600},
        {"name": "Armavir", "population": 28900},
        {"name": "Ararat", "population": 20300},
        {"name": "Artashat", "population": 20700}
    ]

    sorted_cities = sorted(cities, key=lambda x: x["population"], reverse=True)

    top_10_cities = sorted_cities[:10]

    return jsonify(top_10_cities)


if __name__ == '__main__':
    app.run()
