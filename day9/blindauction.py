import os
from art import logo

def clear_console():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_winner(bids):
    """Calculate the winner of the auction."""
    highest_bidder = max(bids, key=bids.get)
    highest_bid = bids[highest_bidder]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

def get_bid():
    """Get a bid from a user."""
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    return name, bid

def auction():
    """Run the auction."""
    bids = {}
    while True:
        name, bid = get_bid()
        bids[name] = bid
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue.lower() != "yes":
            break
        clear_console()
    clear_console()
    calculate_winner(bids)

if __name__ == "__main__":
    clear_console()
    print(logo)
    print("Welcome to the secret auction program.")
    auction()