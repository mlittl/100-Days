import random as r


def main():
    names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
    names = names_string.split(", ")
    choice = r.randint(0, len(names) - 1)
    print(f"{names[choice]} is going to buy the meal today!")

if __name__ == '__main__':
    main()