from flask import Blueprint, request, jsonify
from calculations import *

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return 'API Calculator 2.0 running!'

# --- fibonacci's route ---
@routes.route('/fibonacci', methods=['POST'])
def fibonacci_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 3:
        return jsonify({'error': 'You must send exactly 3 values!'})
    try:
        Value1, Value2, limit = map(int, values)
    except ValueError:
        return jsonify({'error':'All values must be integers!'})

    result = fibonacci(Value1, Value2, limit)
    return jsonify(result)
    
# --- factorial's route ---
@routes.route('/factorial', methods=['POST'])
def factorial_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 1:
        return jsonify({'error': 'You must send exactly 1 value!'})
    try:
        Value1 = int(values[0])
    except ValueError:
        return jsonify({'error':'All values must be integers!'})

    result = factorial(Value1)
    return jsonify(result)