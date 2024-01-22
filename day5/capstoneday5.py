#Password Generator Project
import random


def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""
    new_password = []

    for _ in range(nr_letters):
        password += random.choice(letters)
    for _ in range(nr_symbols):
        password += random.choice(symbols)
    for _ in range(nr_numbers):
        password += random.choice(numbers)

    for char in password:
        new_password.append(char)
    random.shuffle(new_password)

    password = "".join(new_password)
    return password

def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(password)

if __name__ == "__main__":
    main()