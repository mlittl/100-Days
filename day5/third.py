
# You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.


def main():
    target = int(input("Enter a number between 0 and 1000: "))
    
    if target > 1000 or target < 0:
        print("Please enter a number between 0 and 1000")
        return
    
    total = 0
    for i in range(2, target+1, 2):
        total += i
    
    print(total)

if __name__ == "__main__":
    main()