############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# Step 3: User wants to hit?
# If no hit, CPU draws remaining cards until they either bust or win

# Step 4: Showcase winning or losing screen, do you want to play again?
import random 
from typing import Any, Tuple 

def intro() -> str:
    intro = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ")
    if intro == 'y':
        return intro
    else:
        exit()

def game_start(cards) -> Tuple[int, int]:
    from art import logo
    print(logo)
    player_hand = []
    player_hand.append(hit_me(cards))
    player_hand.append(hit_me(cards))
    computer_hand = []
    computer_hand.append(hit_me(cards))
    player_score = sum(player_hand)
    player_hand, player_score = ace_high_or_low(player_hand, player_score)
    winflag = False
    wintext = ""
    result = hit_or_pass(player_hand, computer_hand, player_score)
    while result == 'y':
        if len(result) == 1:
            player_hand.append(hit_me(cards))
            player_score = sum(player_hand)
            player_hand, player_score = ace_high_or_low(player_hand, player_score)
            if player_score > 21:
                winflag, wintext = calculate_winscore(player_hand, computer_hand)
                return (winflag, wintext)
            result = hit_or_pass(player_hand, computer_hand,player_score)
        elif len(result) == 2:
            return (winflag, wintext)
    else:
        winflag, wintext = calculate_winscore(player_hand, computer_hand)
        return (winflag, wintext)
    
def ace_high_or_low(hand, score):
    score = sum(hand)
    if score > 21:
        last_item_in_list = len(hand) - 1
        if hand[last_item_in_list] == 11:
            hand[last_item_in_list] = 1
            score = sum(hand)
            return hand, score
        else:
            return hand, score
    else:
        return hand, score

def hit_me(cards) -> int:
    hit = random.choice(cards)
    return hit

def hit_or_pass(player_hand, computer_hand, score) -> Tuple[Any]:
    winflag = False
    wintext = ""
    print(f"Your cards: {player_hand}, current score: {score} \nComputer's first card: {computer_hand[0]}")
    hitpass = input("Type 'y' to get another card, type 'n' to pass: ")
    if hitpass == 'y':
        return (hitpass)
    else:
        return (winflag, wintext)
    
def calculate_winscore(player_hand, computer_hand):
    player_score = sum(player_hand)
    comp_score = sum(computer_hand)
    player_win = False
    tie = False
    computer_hand, comp_score = comp_turn(computer_hand)
    print(f"   Your final hand: {player_hand}, final score: {player_score}\n   Opponent's final hand: {computer_hand}, final score: {comp_score}")
    if player_score > 21:
        return (player_win, "You went over. You lose 😤")
    elif player_score == comp_score:
        tie = True
        return (player_win, "Draw 🙃")    
    elif player_score == 21:
            player_win = True
            return (player_win, "You win with Blackjack 😎") 
    elif player_score > comp_score and player_score < 21:
        player_win = True
        return (player_win, "You win 😁")   
    elif comp_score > 21:
        return (player_win, "Opponent went over. You win 😁")
    if player_win == False:
        if comp_score == 21:
            return (player_win, "Opponent wins with Blackjack 😤") 
        else:
            return (player_win, "You lose 😤")
    else:
        print("Error")
        exit()

def comp_turn(computer_hand):
    ai_randomizer = random.choice([15,16,17,18,19,20,21])
    comp_score = sum(computer_hand)
    while sum(computer_hand) < ai_randomizer:
        computer_hand = append_to_list(computer_hand, hit_me(cards))
        computer_hand, comp_score = ace_high_or_low(computer_hand, comp_score)
    else:
        comp_score = sum(computer_hand)
        return computer_hand, comp_score

def append_to_list(original_list, element_to_add):
    # Create a new list that includes all the original elements
    new_list = [element for element in original_list]
    # Add the new element to the end of the new list
    new_list += [element_to_add]
    return new_list

def main():
    global cards
    cards = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    intro()
    result = game_start(cards)
    if result[0] == False and result[1] != "":
        print(result[1])
    elif len(result) == 2 and result[0] == True:
        print(result[1])
    else:
        exit("error")




if __name__ == "__main__":
    main()