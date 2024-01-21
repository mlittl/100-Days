# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

leapcheck = "Not leap year"

if year % 4 == 0:
  leapcheck = "Leap year"
  if year % 100 == 0:
    leapcheck = "Not leap year"
    if year % 400 == 0:
      leapcheck = "Leap year"

print(f"{leapcheck}")
      

