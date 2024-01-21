
import random as r

def random():
    return r.randint(0,1)

def main():
  answer = random()
  if answer == 0:
    print("Tails")
  else:    
    print("Heads")

if __name__ == "__main__":
    main()