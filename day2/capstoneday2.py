#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def calculate_tip(total_bill, tip_percentage):
    return total_bill * tip_percentage / 100

def calculate_bill_per_person(total_bill, tip_percentage, num_people):
    total_tip = calculate_tip(total_bill, tip_percentage)
    total_bill_with_tip = total_bill + total_tip
    return total_bill_with_tip / num_people

def format_amount(amount):
    return "{:.2f}".format(amount)

def main():
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill? $"))
    tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = float(input("How many people to split the bill? "))

    bill_per_person = calculate_bill_per_person(total_bill, tip, people)
    final_amount = format_amount(bill_per_person)

    print(f"Each person should pay: ${final_amount}")

if __name__ == "__main__":
    main()
