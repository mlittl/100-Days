import random
import sys

def join(word_to_join):
    wordjoin = ""
    for item in word_to_join:
        wordjoin += item
    return wordjoin

def player_guess():
    guessing = input("\nGuess a letter: ")
    guessing = guessing.lower()
    return guessing

def guess_checking(guess, word_choice):
    if len(guess) > 1 or guess == " ":
        print("You must guess a single letter")
        return False
    elif guess in word_choice:
        return True
    else:
        print("\n Nope! Hahaha!\n")
        return False
    
def loadword():
    with open('wordlist.txt', 'r') as file:
        word_list = file.readlines()
    #remove any newline characters
    word_list = [word.strip() for word in word_list]
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
    guesses_list = []
    while True:
        gameoverchecklist = print_hangman(spaces, lives)
        guess = player_guess()
        if guess in guesses_list:
            print(f"\nSo far you've guessed: {guesseslist}")
            print("You've already guessed that letter. Try a new one.")
            continue
        guesses_list.append(guess)
        
        if guess_checking(guess, word_choice) == True:
            for letters in range(len(letter_list)): # Replaces the spaces with letters upon successful guess
                if guess in letter_list[letters] and guess != "":
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
        guesseslist = join(guesses_list)
        print(f"\nSo far you've guessed: {guesseslist}")


if __name__ == "__main__":
    main()