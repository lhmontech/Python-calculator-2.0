from flask import Blueprint, request, jsonify
from calculations import *

routes = Blueprint('routes', __name__)

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

# --- tribonacci's route ---
@routes.route('/tribonacci', methods=['POST'])
def tribonacci_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 4:
        return jsonify({'error': 'You must send exactly 4 values!'})
    try:
        Value1, Value2, Value3, limit = map(int, values)
    except ValueError:
        return jsonify({'error':'All values must be integers!'})

    result = tribonacci(Value1, Value2, Value3, limit)
    return jsonify(result)

# --- geometric's route ---
@routes.route('/geometric', methods=['POST'])
def geometric_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 3:
        return jsonify({'error': 'You must send exactly 3 values!'})
    try:
        Value1, Ratio, terms = map(int, values)
    except ValueError:
        return jsonify({'error':'All values must be integers!'})

    result = geometric(Value1, Ratio, terms)
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
        return jsonify({'error':'The value must be integer!'})

    result = factorial(Value1)
    return jsonify(result)

# --- perfect squares's route ---
@routes.route('/squares', methods=['POST'])
def squares_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 2:
        return jsonify({'error': 'You must send exactly 2 values!'})
    try:
        Value1, Value2 = map(int, values)
    except ValueError:
        return jsonify({'error':'All values must be integers!'})

    result = squares(Value1, Value2)
    return jsonify(result)

# --- prime numbers's route ---
@routes.route('/primes', methods=['POST'])
def primes_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 2:
        return jsonify({'error': 'You must send exactly 2 values!'})
    try:
        Value1, Value2 = map(int, values)
    except ValueError:
        return jsonify({'error':'All values must be integers!'})

    result = primes(Value1, Value2)
    return jsonify(result)

# --- alternating sequence's route ---
@routes.route('/alternating', methods=['POST'])
def alternating_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 2:
        return jsonify({'error': 'You must send exactly 2 values!'})
    try:
        Value1, terms = map(int, values)
    except ValueError:
        return jsonify({'error':'All values must be integers!'})

    result = alternating(Value1, terms)
    return jsonify(result)

# --- cubes's route ---
@routes.route('/cubes', methods=['POST'])
def cubes_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 2:
        return jsonify({'error': 'You must send exactly 2 values!'})
    try:
        Value1, Value2 = map(int, values)
    except ValueError:
        return jsonify({'error':'All values must be integers!'})

    result = cubes(Value1, Value2)
    return jsonify(result)

# --- binary's route ---
@routes.route('/binary', methods=['POST'])
def binary_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 1:
        return jsonify({'error': 'You must send exactly 1 value!'})
    try:
        Value1 = int(values[0])
    except ValueError:
        return jsonify({'error':'The value must be integer!'})

    result = binDecimal(Value1)
    return jsonify(result)

# --- hexadecimal's route ---
@routes.route('/hexadecimal', methods=['POST'])
def hexadecimal_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 1:
        return jsonify({'error': 'You must send exactly 1 value!'})
    try:
        Value1 = int(values[0])
    except ValueError:
        return jsonify({'error':'The value must be integer!'})

    result = hexaDecimal(Value1)
    return jsonify(result)

# --- common calculation's route ---
@routes.route('/common', methods=['POST'])
def common_route():
    data = request.get_json()
    
    values = data.get('values', [])
    if not values:
        return jsonify({'error': 'You must send an expression!'})
    expression = str(values[0])
    try:    
        result = common(expression)
        return jsonify(result)
    except TypeError:
        return jsonify({'error': 'Enter a valid expression!'})
    except ZeroDivisionError:
        return jsonify({'error': 'It is not possible to divide by zero!'})
    except Exception:
        return jsonify({'error': 'Unexpected error!'})

# --- triangular's route ---
@routes.route('/triangular', methods=['POST'])
def triangular_route():
    data = request.get_json()
    values = data.get('values', [])
    if len(values) != 1:
        return jsonify({'error': 'You must send exactly 1 value!'})
    try:
        Value1 = int(values[0])
    except ValueError:
        return jsonify({'error':'The value must be integer!'})

    result = triangular(Value1)
    return jsonify(result)