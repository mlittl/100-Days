 ## Overview

This code snippet demonstrates a simple Python program that manages a travel log. The main part of the code includes defining the variables `country`, `visits` and `list_of_cities` with their corresponding values, then using these to create an entry in the `travel_log` list.

## Learnings

### Beginner level

1. **Variable Declaration**: In Python, variables can be declared by assigning a value to it. For example: `country = "Brazil"`
2. **Input Function**: The `input()` function is used to prompt the user for input and returns the input as a string. It's used in this program to get values for the `country`, `visits` and `list_of_cities`.
3. **List Creation**: Lists in Python are created using square brackets, with each item separated by commas. For example: `list_of_cities = ["Sao Paulo", "Rio de Janeiro"]`
4. **Dictionary Creation**: In Python, dictionaries are used to store data values in key-value pairs. Dictionaries are created using curly brackets and each item is separated by a comma. For example: `{"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]}`
5. **List Manipulation**: Lists can be manipulated in various ways in Python, such as appending an item to the end of a list using the `append()` function. For example: `travel_log.append({"country": country, "visits":visits, "cities":list_of_cities})`

### Advanced level

1. **Function Definition**: In Python, functions are defined using the `def` keyword followed by the function name and a pair of parentheses. For example: `def add_new_country(country, visits, list_of_cities):`. The code inside the function is indented to show that it belongs to the function.
2. **Function Invocation**: Functions are invoked or called by their name followed by a pair of parentheses containing the arguments to be passed to the function. For example: `add_new_country(country, visits, list_of_cities)`
3. **Formatting Strings**: In Python, strings can be formatted using the `f-string` syntax. This allows you to embed expressions inside string literals, with the expressions delimited by curly braces. For example: `print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")`

### Expert level

1. **Code Comments**: Python supports single-line comments using the `#` symbol, which is used throughout this code snippet to document and explain what each section of code does. This is a good practice for writing maintainable code.
2. **String Conversion**: The `int()` function is used to convert a string input into an integer. For example: `visits = int(input())`. This is useful when you need to use numeric data in your program that has been provided by the user as a string.
3. **Code Encapsulation**: By creating a function (`add_new_country`) which accepts the necessary parameters and appends the new country information to the `travel_log` list, the code is well-encapsulated and easy to maintain. This is a good practice when writing reusable code.

## Conclusion

This code snippet provides a solid foundation for managing a travel log in Python, teaching beginners how to declare variables, use the `input()` function, create lists and dictionaries, manipulate lists, define functions, and format strings. Advanced users can learn more about string conversion, code comments, and encapsulation. Overall, this is an excellent learning tool for anyone looking to improve their Python coding skills.

-----
# Instructions

You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])

DO NOT modify the travel_log directly. The goal is to create a function that modifies it.
Example Input

Brazil
5
["Sao Paulo", "Rio de Janeiro"]

## Example Output

I've been to Brazil 5 times.
My favourite city was Sao Paulo.

## Hint

    Look at the function call above to see what the name of the function should be.

    The inputs for the function are positional arguments. The order is very important.

    Feel free to choose your own parameter names.

