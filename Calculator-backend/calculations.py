def fibonacci():
    try:
        Value1 = int(input('Enter the first number: '))
        Value2 = int(input('Enter the second number: '))
        limit = int(input('Enter the limit: '))
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
    except ValueError:
            return 'Error! Enter a valid number!'


print(fibonacci())