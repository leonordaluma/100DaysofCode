def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)

    end_calculating = False
    while end_calculating is False:
        operation_symbol = input("Pick an operation: ")
        function = operations[operation_symbol]
        num2 = float(input("Enter the next number: "))
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer

        user_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation.: ")
        if user_input != 'y':
            end_calculating = True
            calculator()

calculator()