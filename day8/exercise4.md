# Overview
This program is designed to check whether a given integer `n` is prime or not. The program prompts the user for an input, converts it into an integer, and passes it as an argument to the `prime_checker()` function. The function then checks whether the number is prime or not based on the conditions defined within the function.

# Learnings
To understand how this code works, we need to break down the function step by step:

1. The `prime_checker(number)` function takes a single argument, `number`, which represents the integer that needs to be checked for primality.
2. The first conditional statement (`if number % 1 == 0:`) checks if the input is an integer. If it's not, the function prints "It's not a prime number." and exits.
3. The next conditional statement (`if number % number == 0:`) checks if the input is divisible by itself, which would make it a composite number. In this case, the function prints "It's not a prime number." and exits.
4. The third conditional statement (`if number % 3 != 0:`) checks if the input is divisible by 3. If it is, the function concludes that it's not a prime number and proceeds to print "It's not a prime number." and exit.
5. If none of these conditions are met, the function prints "It's a prime number." and exits.
6. Finally, the program prompts the user for input, converts it into an integer (`n = int(input())`), and passes this integer to the `prime_checker()` function.
7. The `prime_checker()` function is called with the argument `number=n`, which effectively checks whether the user-provided input `n` is a prime number or not.

# Conclusion
Through this learning experience, we have gained an understanding of how to check for primality in integers using simple conditional statements within a function. This knowledge can be applied to various programming tasks that require checking whether a given integer is prime or not. Additionally, this exercise has improved our coding skills by allowing us to apply and deepen our understanding of basic Python programming concepts like functions, conditionals, and input/output handling.

-----
# Instructions Below

Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

## Example Input 1

73

## Example Output 1

It's a prime number.

## Example Input 2

75

## Example Output 2

It's not a prime number.
