print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

def main():
  totalbill = 0
  if size == "S":
    totalbill = 15
  elif size == "M":
    totalbill = 20
  elif size == "L":
    totalbill = 25
  
  if add_pepperoni != "N" and size == "S":
    totalbill += 2
  if add_pepperoni != "N" and (size == "M" or size == "L"):
    totalbill += 3
  if extra_cheese == "Y":
    totalbill += 1
  print(f"Your final bill is: ${totalbill}.")
  
if __name__ == "__main__":
    main()