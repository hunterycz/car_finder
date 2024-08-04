from flask import Flask, jsonify, send_from_directory
from car_classes.autotrader import AutoTrader
from car_classes.cargurus import CarGurus
from car_classes.cars_com import CarsCom
from car_classes.edmunds import Edmunds

app = Flask(__name__)

@app.route('/url_generator', methods=['GET'])
def url_generator():
    urls = []
    urls.extend(AutoTrader().generate_urls())
    urls.extend(CarGurus().generate_urls())
    urls.extend(CarsCom().generate_urls())
    urls.extend(Edmunds().generate_urls())

    return jsonify(urls)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=500)
