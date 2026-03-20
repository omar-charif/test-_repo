def add_two_numbers(a, b):
    return a + b

def multiply_two_numbers(a, b):
    return a * b

def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def operate_on_numbers(a, b, operation):
    if operation == 'add':
        return add_two_numbers(a, b)
    elif operation == 'multiply':
        return multiply_two_numbers(a, b)
    elif operation == 'divide':
        return divide_two_numbers(a, b)
    else:
        raise ValueError("Unsupported operation")

if __name__ == "__main__":
    print(operate_on_numbers(10, 5, 'add'))       # Output: 15
    print(operate_on_numbers(10, 5, 'multiply'))  # Output: 50
    print(operate_on_numbers(10, 5, 'divide'))    # Output: 2.0