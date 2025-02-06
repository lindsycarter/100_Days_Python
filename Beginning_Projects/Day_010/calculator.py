from calculator_art import logo


# Create functions for +, -, *, /
def add(n1, n2):
    """Returns the SUM of number 1 and number 2"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts number 2 from number 1"""
    return n1 - n2


def multiply(n1, n2):
    """Returns the PRODUCT of number 1 and number 2"""
    return n1 * n2


def divide(n1, n2):
    """Divides number 1 by number 2"""
    return n1 / n2


# dictionary of the 4 functions as VALUES, KEYS are the operand symbols
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            # replace with a clear() function
            print("\n * 20")
            calculator()


calculator()
