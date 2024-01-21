import random as r

def user_choice(rock,paper,scissors):
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)
    else:
        print("You typed an invalid number, you lose!")
    return choice

def computer_choice(rock,paper,scissors):
    choice = r.randint(0,2)
    print("Computer chose:")
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)
    return choice


def print_victory_condition(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("""
        Congratulations! You are the champion!
         ___________
        '._==_==_=_.'
        .-\:      /-.
       | (|:.     |) |
        '-|:.     |-'
          \::.    /
           '::. .'
             ) (
           _.' '._
         |__WINNER__|
        """)
    elif user_choice == 2 and computer_choice == 0 or (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2):
        print("""
        _____      
        |   |
        | L |     
        | O |     
        | S |     
        | E | 
        | R |_____
        |_________|      
        """)
    return

def main():
    
    rock = '''
       _______
    ----'   ____)
    -    (_____)
    -    (_____)
    -  -  (____)
    ----.__(___)
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
    user = user_choice(rock,paper,scissors)
    computer = computer_choice(rock,paper,scissors)
    print_victory_condition(user, computer)

if __name__ == "__main__":
    main()