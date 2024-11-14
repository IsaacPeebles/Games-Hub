def better_calc():
    print('This is a calculator')

    while True:
        num1 = float(input('Please enter your first number: '))
        op = input('Please select your operation: add, subtract, multiply, divide: ').lower()
        num2 = float(input('Please enter your second number: '))

        operations_key = {
            'add': lambda num1, num2: num1 + num2,
            'subtract': lambda num1, num2: num1 - num2,
            'multiply': lambda num1, num2: num1 * num2,
            'divide': lambda num1, num2: num1 / num2 if num2 != 0 else 'Divide by zero error',
        }

        result = operations_key.get(op, lambda num1, num2: 'That is not a valid operation, please select from the given list')(num1, num2)
        print(result)

        clear = input('Clear? [y/n]: ').lower()
        if clear == 'y':
            continue
        elif clear == 'n':
            print('Clear')
            break
        else:
            print("Please enter 'y' or 'n'")

better_calc()