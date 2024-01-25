# Step 1 
import random

def player_guess():
    guessing = input("Guess a letter!\n")
    guessing = guessing.lower()
    return guessing

def guess_checking(guess, word_choice):
    guess_check = False
    while True:
        if guess in word_choice:
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
        spaces.append("__ ")
    return spaces

def setup_letterlist(word_choice):
    letter_list = []
    for letters in word_choice:
        letter_list.append(letters)
    return letter_list

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
    while True:
        print_hangman(spaces)
        guess = player_guess()
        if guess_checking(guess, word_choice) == True:
            for letters in range(len(letter_list)):
                spaces[letters] = letter_list[letters]
        else:
            print("You guessed wrong")
            winloss_counter += 1
            if winloss_counter == 5:
                print("GAME OVER")
                break
            print_hangman(spaces)





if __name__ == "__main__":
    main()