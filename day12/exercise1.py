import random
from typing import Tuple

def difficulty() -> str:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficulty

def remaining_guesses(guesses) -> int:
    print(f"You have {guesses} attempts remaining to guess the number")
    return guesses

def create_answer() -> Tuple[int]:
    possible_answers = []
    for i in range(0, 100, 1):
        possible_answers.append(i)
    answer = (random.choice(possible_answers))
    return answer

def check_guess(guess, answer) -> list[str, bool]:
    if guess == answer:
        return ["You won!", True] 
    elif guess < answer:
        return ["Too low", False]
    elif guess > answer:
        return ["Too high", False]

def user_guess_validation() -> list[str, bool]:
    guess = input("Make a guess: ")
    try: 
        guess = int(guess)
        if guess > 0 and guess <= 100:
            return [guess, True]
        else:
            return [guess, False]
    except:
        print("Error, Restarting") 
        main()


def end_game_loop(won_or_lost) -> bool:
    restart = input("If you'd like to play again, type 'y'. Otherwise, type 'n': ")
    if restart == "y":
        return True
    else:
        return False

def game_loop(guesses, answer): 
    remaining_guesses(guesses)
    user_guess = user_guess_validation()
    if True in user_guess:
        #Immediate Win condition check
        guess_check = check_guess(user_guess[0], answer)
        print(guess_check[0])
        if True in guess_check:
            if end_game_loop() == True:
                main()
            else:
                print("Bye for now! Thanks for playing.")
                exit()
        #If they didn't immediately win..
        else:
            print("Guess again.")
            guesses -= 1
            if guesses <= 0:
                print("You lost :(")
                end_game_loop()
            game_loop(guesses, answer)
    else:
        print("Make sure to choose a valid number")
        guesses -= 1
        game_loop(guesses, answer)



def game_start():
    from art import logo 
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    answer = create_answer()
    diff = difficulty()
    if diff == 'easy':
        guesses = 10
        game_loop(guesses, answer)

    elif diff == 'hard':
        guesses = 5
        game_loop(guesses, answer)
    else:
        print("Invalid input, restarting")
        main()



def main():
    game_start()

if __name__ == "__main__":
    main()