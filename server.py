from flask import Flask, jsonify, send_from_directory, abort
from car_classes.autotrader import AutoTrader  # Import your existing scripts here
from car_classes.cargurus import CarGurus
from car_classes.cars_com import CarsCom
from car_classes.edmunds import Edmunds
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/url_generator', methods=['GET'])
def url_generator():
    try:
        urls = [
            {
                "name": "CarGurus",
                "urls": CarGurus().generate_urls_webpage()
            },
            {
                "name": "AutoTrader",
                "urls": AutoTrader().generate_urls_webpage()
            },
            {
                "name": "Cars.com",
                "urls": CarsCom().generate_urls_webpage()
            },
            {
                "name": "Edmunds",
                "urls": Edmunds().generate_urls_webpage()
            }
        ]

        return jsonify(urls)
    except Exception as e:
        app.logger.error(f"Error generating URLs: {e}")
    app.logger.debug(f"Generated URLs: {urls}")
    return jsonify(urls)


@app.route('/')
def index():
    try:
        return send_from_directory('frontend', 'index.html')
    except FileNotFoundError:
        app.logger.error('index.html not found')
        abort(404)


@app.route('/styles.css')
def styles():
    try:
        return send_from_directory('frontend', 'styles.css')
    except FileNotFoundError:
        app.logger.error('styles.css not found')
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500)