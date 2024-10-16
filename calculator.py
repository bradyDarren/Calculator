# creation of functions designed to perform the basic functions of a calculator. 
def add (n1, n2):
    # if type(n1) != 
    return (n1 + n2)

def subtract (n1, n2):
    return (n1 - n2)

def multiply (n1, n2):
    return (n1 * n2)

def divide (n1, n2):
    return (n1 / n2)

calc_functions = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def check_number(prompt):
    while True: 
        try: 
            return float(input(prompt))
        except ValueError: 
            print("Invlaid input. Please enter a valid number.")

continue_calc = True

def calculator():
    number1 = check_number("What is the first number?: ")
    
    
    while continue_calc:
        for symbol in calc_functions: 
            print(symbol)
        symbol_choice = input("Pick an operation: ")
        if symbol_choice not in calc_functions:
            print("Please input an appropriate operator.")
            continue

        number2 = check_number("What's the next number?: ")
        result = float(calc_functions[symbol_choice](number1, number2))
        print(f"{number1} {symbol_choice} {number2} = {result}")
        user_choice = input(f"Type 'y' to continue caculating with {result}, or type 'n' to start a new calculation: ")
        if user_choice == 'n':
            print("\n" * 40)
            calculator()
        else:
            number1 = result 
            continue
calculator()