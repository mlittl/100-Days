import random as r

def user_choice(rock,paper,scissors):
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    else:
        print("You typed an invalid number, you lose!")
    return user_choice

def computer_choice(rock,paper,scissors):
    computer_choice = r.randint(0,2)
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)
    return computer_choice

def main():
    
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''
    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    user_choice(rock,paper,scissors)
    print(f"Computer chose:\n")
    computer_choice(rock,paper,scissors)
    

if __name__ == "__main__":
    main()