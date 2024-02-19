## Overview
This code file demonstrates how to create a dictionary of student scores and then use conditional statements to assign grades based on those scores. This practice will help solidify understanding of dictionaries, loops and conditional statements in Python.

## Learnings - Beginner Level
1. **Understanding Dictionaries**: The first part of the code demonstrates how to create a dictionary, which is an unordered collection of data values. Here, it stores student names as keys and their scores as values.
    ```python
    student_scores = {
      "Harry": 81,
      "Ron": 78,
      "Hermione": 99, 
      "Draco": 74,
      "Neville": 62,
    }
    ```
2. **Looping Over Dictionary Values**: The next part of the code uses a for loop to iterate over each key in the dictionary. This is helpful for performing operations on all elements in the dictionary.
    ```python
    for key in student_scores:
        #...
    ```
3. **Using Conditional Statements**: Inside the loop, multiple if statements are used to determine a student's grade based on their score. This helps understand how Python handles boolean logic and conditional branching.
    ```python
    if student_scores[key] >= 91:
        #...
    ```
4. **Creating New Dictionary from Existing Data**: The code also demonstrates how to create a new dictionary (`student_grades`) by extracting and transforming data from another dictionary (`student_scores`). This shows how dictionaries can be used to manipulate existing data.
    ```python
    student_grades[key] = "Outstanding"
    #...
    print(student_grades)
    ```
## Learnings - Advanced Level
5. **Granular Control Over Conditional Statements**: The code uses `and` operator in the conditional statements to define more specific conditions, providing a deeper understanding of how multiple conditions can be used together in Python.
    ```python
    if student_scores[key] >= 81 and student_scores[key] <= 90:
        #...
    ```
6. **Handling Edge Cases**: The code includes a condition for scores less than or equal to 70, which assigns these students the grade "Fail". This demonstrates how edge cases can be handled in programming.
    ```python
    if student_scores[key] <= 70:
        #...
    ```
## Conclusion
The code file offers a practical application of dictionaries, loops and conditional statements in Python for a common scenario - grading students based on their scores. This practice can help expand coding skillset by applying these foundational concepts in a contextual manner.

---------------
# Instructions

You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

    Scores 91 - 100: Grade = "Outstanding"

    Scores 81 - 90: Grade = "Exceeds Expectations"

    Scores 71 - 80: Grade = "Acceptable"

    Scores 70 or lower: Grade = "Fail"

## Expected Output

'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

### Hint

    Remember that looping through a Dictionary will only give you the keys and not the values.

    If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

    At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

