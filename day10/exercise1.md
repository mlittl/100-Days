# Instructions

## Convert the is_leap() functtion

In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

Create a new function called days_in_month()

You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)

And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:

28

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
# Hint

    Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

    Feel free to choose your own parameter names.

    Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

    Be careful with indentation.

-------------

Overview
--------

This project was an excellent opportunity to practice and expand my coding skills, particularly in the area of date and time manipulation. I had to write a function that would determine if a given year is a leap year or not, and then use that function to calculate the number of days in a month for a given year and month.

Learnings
---------

### Beginner Skills

1. Basic understanding of date and time manipulation: This project helped me understand the basics of working with dates and times in Python, including how to calculate the number of days in a month and how to determine if a given year is a leap year or not.
2. Using the modulo operator: I learned how to use the modulo operator (%) to check if a given value is divisible by another value. For example, to check if a year is divisible by 4, we can use the following code: `if year % 4 == 0:`
3. Conditional statements: This project helped me practice using conditional statements (e.g., `if`, `elif`, `else`) to control the flow of my code based on certain conditions.

### Advanced Skills

1. Using the isinstance() function: To determine if a given year is a leap year or not, I had to use the isinstance() function to check if the year is an integer. This allowed me to avoid potential type errors and ensure that my code was working with the correct data type.
2. Creating a custom function: By creating a custom function (is_leap()) to determine if a given year is a leap year or not, I was able to encapsulate this logic and make it reusable across different parts of my code.
3. Using the calendar module: To calculate the number of days in a month, I used the calendar module's month_days() function. This allowed me to easily access pre-defined lists of days for each month of the year, rather than having to hardcode this information myself.

### Expert Skills

1. Using the modulo operator with negative numbers: To determine if a given year is a leap year or not, I had to use the modulo operator with negative numbers (e.g., `year % -4`). This allowed me to handle cases where the year is negative, which is useful when working with dates and times.
2. Handling edge cases: To ensure that my code was robust and handled all possible input values, I had to carefully consider and test for edge cases (e.g., what happens if the year is 0 or 1?). This helped me improve the reliability and accuracy of my code.
3. Writing clear and concise code: To make my code easy to understand and maintain, I aimed to write clear and concise functions and comments. This helped me communicate my intent more effectively and reduce the risk of errors or misunderstandings.

Conclusion
----------

Overall, this project was an excellent opportunity for me to practice and expand my coding skills in a variety of areas. By working through this project, I gained a better understanding of date and time manipulation, conditional statements, and custom functions. Additionally, I was able to develop my expertise in using the modulo operator with negative numbers and handling edge cases. These skills will be valuable as I continue to learn and grow as a developer.