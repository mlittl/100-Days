# Step 1 
import random



word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

def main():
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter!\n")
    guess = guess.lower()


    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    guess_check = False
    letters_guessed = 0
    while True:
        if guess in chosen_word:
            guess_check = True
            print("You got one...\n")
            for letter in chosen_word:
                if guess in letter:
                    #Do I use this to reveal?
                    letters_guessed += 1
            main()
        else:
            print("Nope! Hahaha!\n")
            main()


if __name__ == "__main__":
    main()