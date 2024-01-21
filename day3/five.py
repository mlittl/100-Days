print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

def calculate_true(name1, name2):
    letcalc1 = 0
    for letter in name1:
        if letter == "t" or letter == "T":
            letcalc1 += 1
        elif letter == "r" or letter == "R":
            letcalc1 += 1
        elif letter == "u" or letter == "U":
            letcalc1 += 1
        elif letter == "e" or letter == "E":
            letcalc1 += 1

    for letter in name2:
        if letter == "t" or letter == "T":
            letcalc1 += 1
        elif letter == "r" or letter == "R":
            letcalc1 += 1
        elif letter == "u" or letter == "U":
            letcalc1 += 1
        elif letter == "e" or letter == "E":
            letcalc1 += 1
    return letcalc1
def calculate_love(name1, name2):
        letcalc2 = 0
        for letter in name1:
                if letter == "l" or letter == "L":
                    letcalc2 += 1
                elif letter == "o" or letter == "O":
                    letcalc2 += 1
                elif letter == "v" or letter == "V":
                    letcalc2 += 1
                elif letter == "e" or letter == "E":
                    letcalc2 += 1
        
        for letter in name2:
                if letter == "l" or letter == "L":
                    letcalc2 += 1
                elif letter == "o" or letter == "O":
                    letcalc2 += 1
                elif letter == "v" or letter == "V":
                    letcalc2 += 1
                elif letter == "e" or letter == "E":
                    letcalc2 += 1
        return letcalc2

def main():
    letcalc1 = calculate_true(name1, name2)
    letcalc2 = calculate_love(name1, name2)
    total = str(letcalc1) + str(letcalc2)
    total = int(total)
    if total < 10 or total > 90:
        print(f"Your score is {total}, you go together like coke and mentos.")
    elif 40 <= total <= 50:
        print(f"Your score is {total}, you are alright together.")
    else:
        print(f"Your score is {total}.")

if __name__ == "__main__":
    main()
