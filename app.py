#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/v1.0/temp', methods=['GET'])
def get_temp():
    return jsonify({'temperatura': 21, 'humidity': 52})

@app.route('/api/v1.0/carbon', methods=['GET'])
def get_carbon():
    return jsonify({'deadly': False})

@app.route('/api/v1.0/motor', methods=['GET'])
def move_motor():
    return jsonify({'message', 'Succes'})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8000, debug=True)
