def fibonacci(Value1, Value2, limit):
        if limit < (Value1 or Value2):
            return 'Invalid limit! Enter a limit greater than the initial values!'
        elif Value1 == 0 and Value2 == 0:
            return f'Error! You entered {Value1} for both values, this creates an infinite sequence!'
        else:
            fibonacciList = []
            while Value1 <= limit:
                fibonacciList.append(Value1)
                next = Value1 + Value2
                Value1 = Value2
                Value2 = next
            return ' '.join(map(str, fibonacciList))

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


def geometric(Value1, Ratio, limit):
    if Ratio == 1 or Ratio == 0 or Ratio == -1:
        return f'Error! You entered {Ratio} as the ratio, this creates an infinite sequence!'
    else:
        geometricList = []
        while Value1 <= limit:
            geometricList.append(Value1)
            Value1 = Value1 * Ratio
        return ' '.join(map(str, geometricList))

def factorial(Value1):
    if Value1 <= 0:
        return 'Factorial is not defined for negative numbers'
    else:
        numbers = []
        result = 1
        for i in range(1, Value1 + 1):
            result = result * i
            numbers.append(i)
        return result

def squares(Value1, Value2):
    if Value1 > Value2:
        print('Invalid limit! Enter a limit greater than the initial value!')
    else:
        squaresList = []
        print('The perfect squares within the interval you defined are:')
        for i in range(Value1, Value2 + 1):
            result = i ** 2
            squaresList.append(result)
            i += 1
        return ' '.join(map(str, squaresList))

try:
    Value1 = int(input('Enter the number: '))
    Value2 = int(input('Enter the number: '))
except ValueError:
            print('Error! Enter a valid number!')

result = squares(Value1, Value2)
print(result)