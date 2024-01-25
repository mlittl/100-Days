# Step 1 
import random
import sys

def player_guess():
    guessing = input("Guess a letter!\n")
    guessing = guessing.lower()
    return guessing

def guess_checking(guess, word_choice):
    guess_check = False
    while True:
        if len(guess) > 1 or len(guess) < 0 or guess != str:
            print("You must guess a single letter")
            break
        if guess == "":
            print("You must guess a single letter")
            break
        elif guess in word_choice:
            guess_check = True
            print("You got one...\n")
            return guess_check
        else:
            print("Nope! Hahaha!\n")
            return guess_check

def loadword():
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    return chosen_word

def setup_spaces(word_choice):
    spaces = []
    for letters in word_choice:
        spaces.append("_")
    return spaces

def setup_letterlist(word_choice):
    letter_list = []
    for letters in word_choice:
        letter_list.append(letters)
    return letter_list

def victory_check(guesses_dict, word_choice):
    if guesses_dict >= 5:
        print("Game Over! Man has Hang'd")
        sys.exit()


def print_hangman(spaces):
    
    gallows = [
        "  _______",
        "  |     ",
        "  |     ",
        "  |     ",
        "  |     ",
        "__|__"
    ]
    for line in gallows:
        print(line)    
    spacesjoined = ""
    for item in spaces:
        spacesjoined += item
    print(spacesjoined)

    

def main():
    print("Welcome to Hangman")
    word_choice = loadword()
    spaces = setup_spaces(word_choice)
    letter_list = setup_letterlist(word_choice)
    winloss_counter = 0
    guesses_count = 0
    guesses_dict = {}
    while True:
        print_hangman(spaces)
        guess = player_guess()
        guesses_count += 1
        guesses_dict[guess] = guesses_count
        if guess_checking(guess, word_choice) == True:
            for letters in range(len(letter_list)):
                if guess in letter_list[letters]:
                    spaces[letters] = letter_list[letters]
                    if spaces == letter_list:
                        print("You win!")
                        sys.exit()
        else:
            winloss_counter += 1
            if winloss_counter == 5:
                print("GAME OVER")
                break
            print_hangman(spaces)





if __name__ == "__main__":
    main()