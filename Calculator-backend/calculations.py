# --- fibonacci's function ---
def fibonacci(Value1, Value2, limit):
    if limit < (Value1 or Value2):
        return {'error':'Invalid limit! Enter a limit greater than the initial values!'}
    elif Value1 == 0 and Value2 == 0:
        return {'error': 'Both initial values cannot be zero, this creates an infinite sequence!'}
    else:
        fibonacciList = []
        while Value1 <= limit:
            fibonacciList.append(Value1)
            next = Value1 + Value2
            Value1 = Value2
            Value2 = next
        return {'sequence': fibonacciList}

# tribonacci's function
def tribonacci(Value1, Value2, Value3, limit):
    if Value1 == 0 and Value2 == 0 and Value3 == 0:
        return f'Error! You entered {Value1} for all three values, this creates an infinite sequence!'
    elif limit < (Value1 or Value2 or Value3):
        return 'Invalid limit! Enter a limit greater than the initial values!'
    else:
        tribonacciList = []
        while Value1 <= limit:
            tribonacciList.append(Value1)
            next = Value1 + Value2 + Value3
            Value1 = Value2
            Value2 = Value3
            Value3 = next
        return ' '.join(map(str, tribonacciList))


def geometric(Value1, Ratio, Value2):
    if Ratio == 1 or Ratio == 0 or Ratio == -1:
        return f'Error! You entered {Ratio} as the ratio, this creates an infinite sequence!'
    else:
        geometricList = []
        for i in range(Value1, Value2 + 1):
            geometricList.append(Value1)
            Value1 = Value1 * Ratio
        return ' '.join(map(str, geometricList))

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


def squares(Value1, Value2):
    if Value1 > Value2:
        print('Invalid limit! Enter a limit greater than the initial value!')
    else:
        squaresList = []
        print('The perfect squares within the interval you defined are:')
        for i in range(Value1, Value2 + 1):
            result = i ** 2
            if (result >= Value1) and (result <= Value2):
                squaresList.append(result)
            i += 1
        return ' '.join(map(str, squaresList))

def primes(Value1, Value2):
    primesList = []
    if Value1 > Value2:
        print('Invalid limit! Enter a limit greater than the initial value!')
    else:
        print('The prime numbers within the interval you defined are:')
        for i in range(Value1, Value2 + 1):
            is_prime = i > 1
            for j in range(2, i - 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primesList.append(i)
    return ' '.join(map(str, primesList))

def alternating(Value1, Value2):
    if Value1 > Value2:
        print('Invalid limit! Enter a limit greater than the initial value!')
    else:
        alternatingList = []
        print('The alternating sequence within the interval you defined is:')
        for i in range(Value1, Value2 + 1):
            alternatingList.append(Value1)
            Value1 = Value1 * 2
            Value1 = Value1 * -1
        return ' '.join(map(str, alternatingList))

def cubes(Value1, Value2):
    if Value1 > Value2:
        print('Invalid limit! Enter a limit greater than the initial value!')
    else:
        cubesList = []
        print('The cubes within the interval you defined are:')
        for i in range(Value1, Value2 + 1):
            result = i ** 3
            cubesList.append(result)
            i += 1
        return ' '.join(map(str, cubesList))

def binDecimal(Value1):
    if Value1 == 0:
        return '0 = 0'
    else:
        binaryList = []
        while Value1 > 0:
            binary = Value1 % 2
            binaryList.append(binary)
            Value1 = Value1 // 2
        return ''.join(map(str, binaryList[::-1]))

def hexaDecimal(Value1):
    if Value1 == 0:
        return '0 = 0'
    else:
        hexaMap = '0123456789ABCDEF'
        hexaList = []
        while Value1 > 0:
            hexa = Value1 % 16
            hexaList.append(hexaMap[hexa])
            Value1 = Value1 // 16
        return ''.join(map(str, hexaList[::-1]))
