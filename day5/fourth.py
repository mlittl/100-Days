from time import sleep


def main():
    total = 100
    for i in range(1, total+1, 1):
        sleep(0.1)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
            continue
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
            continue
        else:
            print(i)
            continue



if __name__ == "__main__":
    main()