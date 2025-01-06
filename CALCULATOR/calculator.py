from art import logo

print(logo)
#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


#Operations dict
operations = {"+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : divide
              }

#Input
def calculator():
    num1 = int(input("What's the first number? "))

    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:
        symbol = input("Choose an operation: ")
        num2 = int(input("What's the next number? "))

        calculation_function = operations[symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        repeat = input(f"Press 'y' to continue with {answer} or 'r' to restart or 'n' to exit: ") 
        if repeat == "y":
            num1 = answer
        elif repeat == "r":
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()
