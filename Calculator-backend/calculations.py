# --- fibonacci's function ---
def fibonacci(Value1, Value2, limit):
    if limit < (Value1 or Value2):
        return {'error':'Invalid limit! Enter a limit greater than the initial values!'}
    elif Value1 <= 0 and Value2 <= 0:
        return {'error': 'Both initial values cannot be zero or negative, this creates an infinite sequence!'}
    else:
        fibonacciList = []
        while Value1 <= limit:
            fibonacciList.append(Value1)
            next = Value1 + Value2
            Value1 = Value2
            Value2 = next
        return {'sequence': fibonacciList}

# --- tribonacci's function ---
def tribonacci(Value1, Value2, Value3, limit):
    if Value1 <= 0 and Value2 <= 0 and Value3 <= 0:
        return {'error':'The three initial values cannot be zero or negative, this creates an infinite sequence!'}
    elif limit < (Value1 or Value2 or Value3):
        return {'error':'Invalid limit! Enter a limit greater than the initial values!'}
    else:
        tribonacciList = []
        while Value1 <= limit:
            tribonacciList.append(Value1)
            next = Value1 + Value2 + Value3
            Value1 = Value2
            Value2 = Value3
            Value3 = next
        return {'sequence': tribonacciList}

# --- geometric's function ---
def geometric(Value1, Ratio, Value2):
    if Ratio == 1 or Ratio == 0 or Ratio == -1:
        return {'error': f'You entered {Ratio} as the ratio, this creates an infinite sequence!'}
    else:
        geometricList = []
        for i in range(Value1, Value2 + 1):
            geometricList.append(Value1)
            Value1 = Value1 * Ratio
        return {'sequence': geometricList}

# --- factorial's function ---
def factorial(Value1):
    if Value1 <= 0:
        return {'error':'Factorial is not defined for negative numbers'}
    else:
        numbers = []
        result = 1
        for i in range(1, Value1 + 1):
            result = result * i
            numbers.append(i)
        return {'result': result}

# --- function of perfect squares ---
def squares(Value1, Value2):
    if Value1 > Value2:
        return {'error':'Invalid limit! Enter a limit greater than the initial value!'}
    else:
        squaresList = []
        for i in range(Value1, Value2 + 1):
            result = i ** 2
            if (result >= Value1) and (result <= Value2):
                squaresList.append(result)
            i += 1
        return {'sequence': squaresList}

# --- function of prime numbers ---
def primes(Value1, Value2):
    primesList = []
    if Value1 > Value2:
        return {'error':'Invalid limit! Enter a limit greater than the initial value!'}
    elif (Value1 or Value2) <= 0:
        return {'error':'Prime numbers are not defined for negatives'}
    else:
        for i in range(Value1, Value2 + 1):
            is_prime = i > 1
            for j in range(2, i - 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primesList.append(i)
    return {'sequence': primesList}

# --- alternating sequence's function ---
def alternating(Value1, Value2):
    if Value1 > Value2:
        return {'error':'Invalid limit! Enter a limit greater than the initial value!'}
    else:
        alternatingList = []
        for i in range(Value1, Value2 + 1):
            alternatingList.append(Value1)
            Value1 = Value1 * 2
            Value1 = Value1 * -1
        return {'sequence': alternatingList}

# --- function of cubes ---
def cubes(Value1, Value2):
    if Value1 > Value2:
        return {'error':'Invalid limit! Enter a limit greater than the initial value!'}
    else:
        cubesList = []
        for i in range(Value1, Value2 + 1):
            result = i ** 3
            cubesList.append(result)
            i += 1
        return {'sequence': cubesList}

# --- function decimal to binary ---
def binDecimal(Value1):
    if Value1 <= 0:
        return {'error':'Is not defined for negative numbers'}
    else:
        binaryList = []
        while Value1 > 0:
            binary = Value1 % 2
            binaryList.append(binary)
            Value1 = Value1 // 2
        return {'sequence': ''.join(map(str, binaryList[::-1]))}

# --- function decimal to hexadecimal ---
def hexaDecimal(Value1):
    if Value1 <= 0:
        return {'error':'Is not defined for negative numbers'}
    else:
        hexaMap = '0123456789ABCDEF'
        hexaList = []
        while Value1 > 0:
            hexa = Value1 % 16
            hexaList.append(hexaMap[hexa])
            Value1 = Value1 // 16
        return {'sequence': ''.join(map(str, hexaList[::-1]))}
