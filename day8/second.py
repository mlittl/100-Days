def greet(name=input("What's your name? "), location=input("Where are you from? ")):
    print("Hello there " + name + " from " + location)

def main():
    greet() 

if __name__ == "__main__":
    main()