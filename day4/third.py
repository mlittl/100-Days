line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

for letters in position:
  if "A" in position:
    for numbers in position:
      if "1" in position:
        line1[0] = "X"
      elif "2" in position:
        line2[0] = "X"
      elif "3" in position:
        line3[0] = "X"
        
  elif "B" in position:
    for numbers in position:
      if "1" in position:
        line1[1] = "X"
      elif "2" in position:
        line2[1] = "X"
      elif "3" in position:
        line3[1] = "X"
        
  elif "C" in position:
    for numbers in position:
      if "1" in position:
        line1[2] = "X"
      elif "2" in position:
        line2[2] = "X"
      elif "3" in position:
        line3[2] = "X"
        

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")