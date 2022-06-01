#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
import RPi.GPIO as GPIO
from time import sleep
import sys

app = Flask(__name__)
CORS(app)

motor_channel = (29,31,33,35)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(motor_channel, GPIO.OUT)

def move_motor_gpio(di):
    if(di == 0):
        seq = [(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH),
                (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH),
                (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW),
                (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW)]
    else:
        seq = [(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH),
                (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW),
                (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW),
                (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH)]
    for i in range(1024):
        GPIO.output(motor_channel,  seq[i % 4])
        sleep(0.02)


@app.route('/api/v1.0/temp', methods=['GET'])
def get_temp():
    return jsonify({'temperatura': 21, 'humidity': 52})

@app.route('/api/v1.0/carbon', methods=['GET'])
def get_carbon():
    return jsonify({'deadly': False})

@app.route('/api/v1.0/motor', methods=['GET'])
def move_motor():
    move_motor_gpio(0)
    return jsonify({'message', 'Succes'})

@app.route('/api/v1.0/motor-l', methods=['GET'])
def move_motor_l():
    move_motor_gpio(1)
    return jsonify({'message': 'Succes'})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8000, debug=True)
