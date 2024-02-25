import art
import game_data
import random 
import os

def clear_console():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(user_input, player1, player2) -> bool:
    if player1['follower_count'] > player2 ['follower_count']:
        if user_input == 'A':
            return True
        else:
            return False
    elif player2['follower_count'] > player1['follower_count']:
        if user_input == 'B':
            return True
        else:
            return False
    else:
        print("Something went wrong in Compare")
        exit()


def game_loop():
    result = True
    wintally = 0
    while result == True:
        clear_console()
        print(art.logo)
        if wintally > 0:
            print(f"You're right! Current score: {wintally}.")
        player1 = random.choice(game_data.data)
        player2 = random.choice(game_data.data)
        if player1['name'] == player2['name']:
            player2 = random.choice(game_data.data)
        player1_name = player1['name']
        player1_job = player1['description']
        player1_country = player1['country']
        print(f"Compare A: {player1_name}, {player1_job}, {player1_country}.")
        player2_name = player2['name']
        player2_job = player2['description']
        player2_country = player2['country']
        print(art.vs)
        print(f"Compare B: {player2_name}, {player2_job}, {player2_country}.")    
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        if user_input == 'A':
            result = compare(user_input, player1, player2)
        elif user_input == 'B':
            result = compare(user_input, player1, player2)    
        else:
            print("Invalid choice, please select A or B")
            main()
        if result == True:
            wintally += 1
        else:
            clear_console()
            print(art.logo)
            print(f"Sorry that's wrong. Final score: {wintally}")
                


def main():
   game_loop()

if __name__ == "__main__":
    main()