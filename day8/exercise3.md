# Overview
This code demonstrates the implementation of a simple function called `paint_calc()`. This function calculates the number of cans of paint required to cover a given area, taking into account the coverage rate of the paint. The user inputs the height and width of the wall in meters, as well as the coverage rate of the paint.

# Learnings
1. **Defining Functions**: In this code, we defined a function called `paint_calc()`. A function is a block of code that performs a specific task. By defining our own functions, we can reuse the same code in multiple places without duplicating it. This promotes code organization and makes the code easier to maintain and understand.
2. **Function Parameters**: The `paint_calc()` function takes three parameters: `height`, `width`, and `cover`. These parameters represent the height, width, and coverage rate of the paint, respectively. By using parameters, we can pass different values to the function each time it is called, allowing for flexibility in the calculations.
3. **Input Data Types**: The code prompts the user to input the height and width of the wall in meters as integers. This ensures that the calculations are accurate, as the area calculation involves multiplication. The coverage rate is hardcoded as 5, which means that for every 5 square meters, one can of paint is required to cover the area.
4. **Calculation and Rounding**: The code calculates the number of cans needed by dividing the total area (height * width) by the coverage rate. To ensure that the correct number of cans is used, the result of the division operation is rounded up using the `math.ceil()` function. This accounts for any minor discrepancies in the coverage rate or wall dimensions.
5. **Printing Output**: Finally, the code prints the number of cans required to cover the area using f-string formatting. The result is displayed as a string within curly braces, replacing the placeholder `{numberofcans}`.

# Conclusion
This learning exercise allowed me to deepen my understanding of defining functions and utilizing their parameters effectively. I also gained experience in handling input data types and performing accurate calculations with them. Additionally, I learned how to round up numbers using the `math.ceil()` function and display output using f-string formatting. Overall, this code has helped me expand my coding skillset and strengthen my knowledge of Python programming.


------------------
# Instructions Listed Below

You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 \* 4) / 5
               = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
Example Input

3
9

Example Output

You'll need 6 cans of paint.

Hint

Stackoveflow link on how to round up a number: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
