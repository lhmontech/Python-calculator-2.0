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
        return jsonify({'Error!': 'You must send exactly 3 values!'})
    Value1, Value2, limit = values
    result = fibonacci(Value1, Value2, limit)
    return jsonify(result)
    