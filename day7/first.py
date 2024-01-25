import random
import sys

def player_guess():
    guessing = input("Guess a letter!\n")
    guessing = guessing.lower()
    return guessing

def join(word_to_join):
    wordjoin = ""
    for item in word_to_join:
        wordjoin += item
    return wordjoin

def guess_checking(guess, word_choice):
    guess_check = False
    while True:
        if len(guess) > 1:
            print("You must guess a single letter")
            break
        if guess == " ":
            print("You must guess a single letter spaces")
            break
        elif guess in word_choice:
            guess_check = True
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

def print_hangman(spaces, lives):
    gallows = [
    '''   
          _______
          |     |
          |     
          |     
          |
          |     
        __|__\n''',
        
    '''   
          _______
          |     |
          |     0
          |     
          |     
          |
        __|__\n''',

    '''   
          _______
          |     |
          |     0
          |     |
          |     |
          |       
          |
        __|__\n''',

    '''   
          _______
          |     |
          |     0
          |     |
          |     |
          |    /  
          |
        __|__\n''',

    '''   
          _______
          |     |
          |     0
          |     |
          |     |
          |    / \ 
          |
        __|__\n''',

    '''   
          _______
          |     |
          |     0
          |    /|
          |     |
          |    / \ 
          |
        __|__\n''',
    
    '''   
          _______
          |     |
          |     0
          |    /|\ 
          |     |
          |    / \ 
          |
        __|__
        
        ### GAME OVER ###
        \n'''
    ]
    print(gallows[lives])
    spacesjoined = join(spaces)
    print(spacesjoined)
    return gallows[lives + 1]

def main():
    print("Welcome to Hangman")
    word_choice = loadword()
    spaces = setup_spaces(word_choice)
    letter_list = setup_letterlist(word_choice)
    lives = 0
    guesses_count = 0
    guesses_dict = {}
    while True:
        gameoverchecklist = print_hangman(spaces, lives)
        guess = player_guess()
        guesses_count += 1
        if guess_checking(guess, word_choice) == True:
            guesses_dict[guess] = guesses_count
            for letters in range(len(letter_list)): # Replaces the spaces with letters upon successful guess
                if guess in letter_list[letters]:
                    spaces[letters] = letter_list[letters]
                    if spaces == letter_list: # Win Condition
                        print("You win!")
                        sys.exit()
        else:
            lives += 1
            if lives >= 6:
                gameovercheck = join(gameoverchecklist)
                print(gameovercheck)
                sys.exit()

if __name__ == "__main__":
    main()