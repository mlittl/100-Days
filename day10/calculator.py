#Calculator

import os
from art import logo

#Clear 
def clear_console():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

#Add
def add(n1, n2):
    return n1+n2

#Subtract
def sub(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

def choose_operation():
    operation_symbol = input("Pick an operation from the line above: ")
    return operation_symbol

def cont(result):
    cont_question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
    return cont_question

def main():
    clear_console()
    print(logo)
    operations = {
        "+":add,
        "-":sub,
        "*":multiply,
        "/":divide
        }
    num1 = float(input("What's the first number?: "))
    for keys in operations:
        print(keys)
    operation_symbol = choose_operation()
    num2 = float(input("What's the second number?: "))
    if operation_symbol in operations:
        result = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
    cont_question = cont(result)
    while cont_question == "y":
        operation_symbol = choose_operation()
        num3 = float(input("What's the next number?: "))
        result = operations[operation_symbol](result, num3)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        cont_question = cont(result)


if __name__ == "__main__":
    main()